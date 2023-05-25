import os
import random
import sys
import logging
from decimal import Decimal, getcontext

from binance.client import Client
from binance.enums import ORDER_TYPE_LIMIT, TIME_IN_FORCE_GTC
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv

load_dotenv()

data = {
    'volume': 1000.0,
    'number': 5,
    'amountDif': 50.0,
    'side': 'SELL',
    'priceMin': 300.0,
    'priceMax': 305.0,
    'symbol': 'BNBUSDT'
}

client = Client(os.getenv('API_KEY'), os.getenv('SECRET_KEY'), testnet=True)


def get_quantity(symbol, amount_usdt):
    """
    Находит текущую стоимость криптовалюты и расчитывает количество(quantity)
    доступное для продажи или покупки.
    """
    ticker = client.get_symbol_ticker(symbol=symbol)
    current_price = Decimal(ticker['price'])
    currency_quantity = Decimal(amount_usdt / current_price)
    return round(currency_quantity, 2)


def get_binance_order(symbol, amount_usdt, price):
    """
    Создаёт ордер в testnet Binance.
    """
    quantity = get_quantity(symbol, Decimal(amount_usdt))
    try:
        order = client.create_order(
            symbol=symbol,
            side=data['side'],
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        return order
    except BinanceAPIException as e:
        logger.error(f"Ошибка в создании ордера: {e}")


def get_amounts_usdt(volume, number, spread):
    """
    Разделяет объём в долларах(volume) на определённое количество(number)
    рандомных частей.
    """
    getcontext().prec = 5
    core_value = Decimal(volume) / Decimal(number)
    amounts = []
    for _ in range(number - 1):
        random_value = Decimal(random.uniform(-spread, spread))
        amounts.append(core_value + random_value)

    last_value = Decimal(volume) - sum(amounts)
    amounts.append(last_value)
    return amounts


def get_prices(min_pr, max_pr, number):
    """
    Расчитывает рандомные цены продажи или покупки в указанном диапазоне.
    """
    return [round(random.uniform(min_pr, max_pr), 2) for _ in range(number)]


def main():
    volume, number = data['volume'], data['number']
    amounts = get_amounts_usdt(volume, number, data['amountDif'])
    prices = get_prices(data['priceMin'], data['priceMax'], number)
    for i in range(len(prices)):
        get_binance_order(data['symbol'], amounts[i], prices[i])
        logger.info(
            f"Создан ордер: {data['side']} {data['symbol']} на {amounts[i]}$"
        )


if __name__ == '__main__':
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=logging.DEBUG,
        format=(log_format),
    )
    handler = logging.StreamHandler(sys.stdout)
    logger = logging.getLogger(__name__)
    main()

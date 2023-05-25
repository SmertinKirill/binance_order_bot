import unittest
from order_bot import (get_amounts_usdt, get_prices, get_quantity,
                       get_binance_order)


class Tests(unittest.TestCase):

    def test_get_binance_order(self):
        order = get_binance_order('BNBUSDT', 100.0, 300.0)
        self.assertIsNotNone(order, 'Не удалось создать ордер')

    def test_get_quantity(self):
        quantity = str(get_quantity('BNBUSDT', 100))
        regex_pattern = r'^[0-9]{1,20}(\.[0-9]{1,20})?$'
        self.assertRegex(
            quantity, regex_pattern, 'Неверный формат значения quantity.'
        )

    def test_get_amounts_usdt(self):
        test_amounts = get_amounts_usdt(100, 4, 15)
        self.assertEqual(
            len(test_amounts), 4, 'Общий объём не разделён на части.'
        )
        self.assertEqual(
            sum(test_amounts), 100, 'Сумма частей не равна volume.'
        )

    def test_get_prices(self):
        test_prices = get_prices(100, 200, 3)
        regex_pattern = r'^([0-9]{1,20})(\.[0-9]{1,20})?$'
        self.assertEqual(
            len(test_prices), 3, 'Общий объём не разделён на части.'
        )
        for price in test_prices:
            self.assertRegex(
                str(price), regex_pattern, 'Неверный формат значения у prices.'
            )
            self.assertGreater(price, 0, 'Цена должна быть больше 0.')


if __name__ == '__main__':
    unittest.main()

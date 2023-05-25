# Binance_order_bot
 Это торговый бот, разработанный для биржи Binance. Бот автоматически дробит заданную сумму на части и размещает ордеры на покупку или продажу заданной криптовалюты. Он основан на API Binance и предоставляет простой способ автоматизировать процесс размещения ордеров на бирже.


## Разработчик
- [SmertinKirill](https://github.com/SmertinKirill)

### Порядок установки
1. Создайте файл `.env` и заполните его, получив тестовые ключи на [testnet.binance.vision](https://testnet.binance.vision/).
    ```
    API_KEY=ваш_ключ
    SECRET_KEY=ваш_секретный_ключ
    ```

2. Создайте виртуальное окружение:
    ```bash
    python -m venv venv
    ```

3. Активируйте виртуальное окружение:
    - Для Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
    - Для Windows:
        ```bash
        venv\Scripts\activate
        ```

4. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

5. В файле `order_bot.py` в словаре `data` можете изменить значения для создания ордеров в соответствии с вашими требованиями.

6. Запустите тесты для проверки функциональности бота:
    ```bash
    python tests.py
    ```

7. Запустите бота:
    ```bash
    python order_bot.py
    ```

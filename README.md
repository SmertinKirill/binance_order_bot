# Binance_order_bot
    Тестовое задание

### Описание проекта Yambd.
Торговый бот предназначен для дробления суммы и размещения ордеров на криптобирже Binance.

## Разработчик
- [SmertinKirill](https://github.com/SmertinKirill)


### Порядок установки
1. В папке инфра создайте файл .env и заполните, тестовые ключи можно получить  по ссылке: https://testnet.binance.vision/ 
```
API_KEY=ваш ключ 
SECRET_KEY=ваш ключ
```
2. Создайте виртуальное окружение ```python -m venv venv```
3. Активируйте виртуальное окружение ```source venv/bin/activate```
4. В файле order_bot.py в  словаре data можете изменить тестовые значения.
5. Запустите тесты ```python tests.py```
6. Запустите бота ```python order_bot.py```

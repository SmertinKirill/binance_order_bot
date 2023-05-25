# Binance_order_bot
Торговый бот предназначен для дробления суммы на части и автоматического размещения ордеров на бирже Binance.

## Разработчик
- [SmertinKirill](https://github.com/SmertinKirill)

### Порядок установки
1. Создайте файл .env и заполните его, тестовые ключи можно получить  по ссылке: https://testnet.binance.vision/ 
```
API_KEY=ваш ключ 
SECRET_KEY=ваш ключ
```
2. Создайте виртуальное окружение ```python -m venv venv```
3. Активируйте виртуальное окружение ```source venv/bin/activate```
4. Установите библиотеки ```pip install -r requirements.txt```
5. В файле order_bot.py в словаре data можете изменить значения для создания ордеров.
6. Запустите тесты ```python tests.py```
7. Запустите бота ```python order_bot.py```

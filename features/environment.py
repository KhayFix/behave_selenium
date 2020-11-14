from apps.web import Web
from apps.connection_db import ConnectionDatabase
from apps.calc import Calculator
from apps.storage import Storage


def browser_init(context):
    """
    context: Behave context
    """
    driver = Web()
    db = ConnectionDatabase()
    calc = Calculator()  # калькулятор для подсчета роста цены
    storage = Storage()

    driver.loc_driver(r'../bin', 'chromedriver.exe')  # расположение драйвера
    driver.options(browser='chrome')  # browser='firefox'
    driver.chrome()  # driver.firefox()
    driver.impl_wait(timeout=5)

    db.create_connection('stocks.db')

    context.driver = driver
    context.db = db  # подключаем нашу базу данных
    context.calc = calc
    context.storage = storage

    context.screenshot_buffer = {}
    context.stock_data = None
    context.collected_data = None


def before_scenario(context, scenario):
    """Выводит название нашего теста при запуске"""

    print("\nStarted scenario :", scenario.name)
    browser_init(context)


def before_step(context, step):
    """Перед каждым шагом выводит название нашего шага"""

    print("\nStarted step: ", step)


def after_step(context, step):
    """Если шаг упадет показывает название нашего шага"""

    if step.status == 'failed':
        print("\nStep failed: ", step)


def after_scenario(context, feature):
    """Удаляет все куки и закрывает браузер"""
    context.driver.delete_all_cookies()
    context.driver.quit()

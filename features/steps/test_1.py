from time import sleep

from behave import when, then, given

# локаторы
MENU_QUOT = "//ul[@class='navMenuUL']/li/a[text()='Котировки']"
MENU_SHARES = "//ul[@class='subMenuNav']/li/a[text()='Акции']"
MENU_RUSSIA = "//ul[@class='main']/li/a[text()='Россия']"
TITLE = "//h1[@class='float_lang_base_1 shortH1 relativeAttr']"
NAME_COMPANY = "//td[@class='bold left noWrap elp plusIconTd']/a"
DATA_PRICE = "//tr/td[3]"  # [:42]


@given("Открытие сайта {url}")
def launch_browser(context, url):
    context.driver.open(url=url)


@when("Поиск меню {name}, появилось выпадающее меню")
def step(context, name):
    object_menu = context.driver.find_by_xpath(MENU_QUOT)
    context.driver.action_chains(object_menu)
    assert name == object_menu.text


@when("Поиск в выпадающем меню '{name}'")
def step(context, name):
    object_menu = context.driver.find_by_xpath(MENU_SHARES)
    context.driver.action_chains(object_menu)
    assert name == object_menu.text


@when("Кликнули на '{name}', перешли в раздел сайта Россия - акции")
def step(context, name):
    object_menu = context.driver.find_by_xpath(MENU_RUSSIA)
    assert name == object_menu.text
    context.driver.action_chains_click(object_menu)


@when("Проверка заголовка '{title}'")
def step(context, title):
    title_object = context.driver.find_by_xpath(TITLE)
    print(title_object.text)
    assert title == title_object.text


@when("Получили  данные из stocks.db : Название, цена")
def step(context):
    context.stock_data = context.db.get_all_from_db('stock_price')
    print(context.stock_data[:10])
    assert context.stock_data


@when("Сбор информации: Название компаний, цена")
def step(context):
    sleep(0.3)
    name_company = context.driver.finds_by_xpath(NAME_COMPANY)
    price_company = context.driver.finds_by_xpath(DATA_PRICE)[:42]
    context.collected_data = [(name.text, price.text)
                              for name, price in zip(name_company, price_company)
                              ]
    assert context.collected_data
    print(context.collected_data[:10])


@when("Получили компании, цена которых повысилась относительно stocks")
def step(context):
    context.calc.add_data_calc(context.stock_data, context.collected_data)
    context.collected_data = context.calc.calc_percent()
    print(context.collected_data[:10])


@when("Сохранение данных в report.json")
def step(context):
    context.collected_data = context.storage.data_conversion(context.collected_data)
    print(context.collected_data)
    context.storage.write_json()


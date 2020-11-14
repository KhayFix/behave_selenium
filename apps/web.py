from selenium import common
from selenium.webdriver import ActionChains

from apps.base_page import BasePage


class Web(BasePage):

    def __init__(self):
        super(Web, self).__init__()

    def open(self, url: str):
        """Открытие ссылки в браузере"""

        try:
            self.driver.get(url=url)
        except TypeError as error:
            print(f'Ошибка -> {error}')
        except common.exceptions.WebDriverException as error:
            print(f'Ошибка -> {error}')

    def impl_wait(self, timeout):
        """Не явное ожидание"""

        self.driver.implicitly_wait(timeout)

    def find_by_xpath(self, xpath: str):
        """Ищет одни элемент на странице."""

        return self.driver.find_element_by_xpath(xpath)

    def finds_by_xpath(self, xpath: str):
        """Ищет все элементы на странице."""

        return self.driver.find_elements_by_xpath(xpath)

    def action_chains(self, object_menu):
        """Открытие выпадающего меню."""

        ActionChains(self.driver).move_to_element(
            object_menu).perform()

    def action_chains_click(self, object_menu):
        """Открытие выпадающего меню и клик по элементу."""

        ActionChains(self.driver).move_to_element(
            object_menu).click().perform()

    def delete_all_cookies(self):
        """Удаляет куки"""

        self.driver.delete_all_cookies()


if __name__ == '__main__':
    web = Web()
    web.loc_driver(r'../bin', 'chromedriver.exe')
    web.options(browser='chrome').chrome()
    web.impl_wait(5)
    web.open("https://ru.investing.com/equities/russia")
    a = web.finds_by_xpath("//tr/td[3]")[:42]
    for x in a:
        print(x.text)
    web.quit()

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class BasePage(object):

    def __init__(self):
        self.object_options = None
        self.location_driver = None
        self.driver = None

    def chrome(self):
        """Работа в браузере хром."""

        self.driver = webdriver.Chrome(
            executable_path=self.location_driver,
            options=self.object_options
        )

    def firefox(self):
        """Работа в браузере фаерфокс."""

        self.driver = webdriver.Firefox(
            executable_path=self.location_driver,
            options=self.object_options
        )

    def options(self, *, browser='chrome'):
        """Запуск настроек браузера.

        По умолчанию Chrome.
        """

        if browser == 'chrome':
            self.object_options = ChromeOptions()
        elif browser == 'firefox':
            self.object_options = FirefoxOptions()

        self.object_options.add_argument('--disable-gpu')

        return self

    def headless(self):
        """Включает безголовый режим."""

        self.object_options.add_argument('--headless')
        return self

    def loc_driver(self, folder: str = None, name_driver: str = None):
        """Расположение до драйверов хром или других для запуска селениума.

        folder - папка в которой храниться драйвер
        name_driver - название драйвера
        """
        base_dir = os.path.abspath(os.path.dirname(__file__))
        self.location_driver = os.path.join(base_dir, folder, name_driver)

    def quit(self):
        """Закрытие браузера."""

        self.driver.quit()


if __name__ == '__main__':
    ca = BasePage()
    ca.loc_driver(r'..\bin', 'chromedriver.exe')
    ca.options().headless().chrome()
    ca.quit()

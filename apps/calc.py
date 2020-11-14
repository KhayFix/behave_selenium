from typing import List, Tuple


class Calculator(object):
    """Считает проценты относительно стоковой цены."""
    _data_stocks = None
    _data_current = None
    _unique_data = None
    _percents = None

    def _sort_data(self):
        """Проверка на уникальность наших _data_stocks и _data_current с помощью множества.

        Если наши полученные данные одинаковые то, вернется False т.к. в множестся храняться только уникальные данные.
        В других случаях сортируем и производим дальнейшую обработку.

        sort() - сортирует полученые данный на лету.
        """

        data = list(set(self._data_stocks + self._data_current))
        if len(data) == len(self._data_stocks):
            return False
        else:
            self._unique_data = []
            self._data_stocks.sort()
            self._data_current.sort()
            return True

    def _percent_count(self, data_stocks: float, data_current: float):
        """Подсчет процентов"""

        try:
            sub = data_current - data_stocks
            self._percents = round(((sub / data_stocks) * 100), 3)
        except ZeroDivisionError as error:
            return f'Деление на ноль -> {error}'

    def _trans_float(self):
        """Преобразование цены акций к float"""

        for data in (self._data_stocks, self._data_current):
            try:
                data_float = [(name, float(value.replace('.', '').replace(',', '.'))) for name, value, *rest in data
                              if type(value) is not float]  # TODO заменить на другой безопасный способ.
                if data_float:
                    if data is self._data_stocks:
                        self._data_stocks = data_float
                    else:
                        self._data_current = data_float

            except ValueError as error:
                print(f'Значение цены должно быть строкой -> {error}')

    def calc_percent(self) -> List[Tuple] or bool:
        """Перебор данный на соответствие роста цены на акции"""

        self._trans_float()
        if self._sort_data():
            for name, value, in self._data_stocks:
                for name_x, value_x, in self._data_current:
                    if name == name_x and value_x > value:
                        self._percent_count(value, value_x)
                        self._unique_data.append((name_x, value_x, self._percents))
            return self._unique_data
        else:
            return False, print("Нет ни одной акции которая изменилась в большую сторону")

    def add_data_calc(self, data_stocks: List[Tuple], data_current: List[Tuple], *, start=False) -> List[Tuple] or bool:
        """Принимает данные следующего типа:

        stock = [('Lenta Ltd', '151,7'), ('Polymetal', '1.497,70')...]
        current = [('Lenta Ltd', '151,7'), ('Polymetal', '1550,70')...]
        """
        self._data_stocks = data_stocks
        self._data_current = data_current
        if start:
            return self.calc_percent()


if __name__ == '__main__':
    stock = [('Lenta Ltd', '151,0'), ('Polymetal', '1.499,70', '1313')]
    test = [('Lenta Ltd', '152,0'), ('Polymetal', '1.497,70')]

    cal = Calculator()
    print(cal.add_data_calc(stock, test, start=True))  # [('Lenta Ltd', 155.7, 2.637)]
    print(cal.calc_percent())  # [('Lenta Ltd', 155.7, 2.637)]

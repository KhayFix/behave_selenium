import json


class Storage(object):
    def __init__(self):
        self._processed_data = None
        self._open = open

    def data_conversion(self, company_data):
        """Преобразует данные в dict.

        Обрабатывает данные следующего вида: [('Lenta Ltd', 221.2, 45.814)]
        в такой вид: {'Lenta Ltd': {'name': 'Lenta Ltd', 'price': 221.2, 'percent': 45.814}
        """

        self._processed_data = {name: {"name": name, "price": price, "percent": percent}
                                for name, price, percent in company_data}
        return self._processed_data

    def write_json(self):
        with self._open("report.json", 'w', encoding='utf-8') as write:
            json.dump(self._processed_data, write, indent=2, ensure_ascii=False)

    def read_json(self):
        with self._open("../report.json", "r", encoding='utf-8') as read:
            print(read.read())


if __name__ == "__main__":
    data = [('Просто слово', 221.2, 45.814), ('Polymetal', 1736.0, 15.911)]
    st = Storage()
    sr = st.data_conversion(data)
    st.write_json()


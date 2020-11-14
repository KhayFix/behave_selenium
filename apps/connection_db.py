import sqlite3
from typing import List, Tuple


class ConnectionDatabase(object):
    """Записывает или забирает(все) данные для указанной таблицы базы данных."""
    _connection = None
    _db_name = None

    def create_connection(self, db_name: str):
        """Создает соединение с БД"""
        self._db_name = db_name
        self._connection = sqlite3.connect(self._db_name)

    def write_data_tuple_db(self, query: str, data: List[Tuple], *, verbose=False) -> bool:
        """
        * query - запрос, который нужно выполнить
        * data - данные, которые надо передать в виде списка кортежей

        Запись кортежа поочереди из списка data.
        Если кортеж удалось записать успешно, изменения сохраняются в БД.
        Если в процессе записи кортежа возникла ошибка, транзакция откатывается.

        Флаг verbose контролирует то, будут ли выведены сообщения об удачной
        или неудачной записи кортежа.
        """

        for row in data:  # TODO вынести в другой метод чтобы при одной ошибки другие данные
            # записывались
            try:
                with self._connection as con:
                    con.execute(query, row)

            except (sqlite3.IntegrityError,
                    sqlite3.OperationalError,
                    sqlite3.ProgrammingError,
                    sqlite3.InterfaceError) as error:
                if verbose:
                    print(f"При записи данный {', '.join(row)} -> Error - {error}")
                return False
            else:
                if verbose:
                    print(f"Запись данных прошла успешна -> {', '.join(row)}")
        return True

    def get_all_from_db(self, table_name: str) -> List[Tuple] or False:
        """Получаем все данные из базы данных"""

        get_all = f"SELECT * FROM {table_name}"
        try:
            with self._connection as con:
                return [data for data in con.execute(get_all)]

        except sqlite3.OperationalError as error:
            print(f'Неудалось получить данные -> {error}')
            return False

    def close_db(self):
        self._connection.close()


if __name__ == "__main__":
    conn = ConnectionDatabase()
    conn.create_connection('stocks.db')
    # a = [('Lenta', '151,7'), ('Polym', '151,7')]
    # b = """INSERT INTO stock_price (name, price) VALUES (?, ?)"""
    # conn.write_data_tuple_db(b, data=a)
    print(conn.get_all_from_db('stock_price'))
    conn.close_db()

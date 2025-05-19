import sqlite3


class Database:
    """
    Класс для работы с БД. тут будут методы для создания таблиц,
    для добавления, обновления и удаления расходов (таблица expenses)
    """

    def __init__(self, path):
        self.path = path

    def create_tables(self):
        """
        Метод, в котором описывается, какие таблицы и с какими колонками создаются для приложения
        """
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    amount REAL
                )
            """)
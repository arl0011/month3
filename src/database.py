import sqlite3

class Database:
    def __init__(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    amount REAL
                )
            """)

    def add_expense(self, name: str, amount: float):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "INSERT INTO expenses (name, amount) VALUES (?, ?)",
                (name, amount)
            )
            conn.commit()

    def all_expenses(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM expenses")
            return result.fetchall()
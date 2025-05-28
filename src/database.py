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

    def count_expenses(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT COUNT(*) FROM expenses")
            return result.fetchone()[0]

    def all_expenses(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM expenses")
            return result.fetchall()

    def get_expense(self, expense_id):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
            return result.fetchone()

    def add_expense(self, name: str, amount: float):
        with sqlite3.connect(self.path) as conn:
            conn.execute("INSERT INTO expenses (name, amount) VALUES (?, ?)", (name, amount))
            conn.commit()

    def update_expense(self, expense_id: int, name: str, amount: float):
        with sqlite3.connect(self.path) as conn:
            conn.execute("UPDATE expenses SET name = ?, amount = ? WHERE id = ?", (name, amount, expense_id))
            conn.commit()

    def delete_expense(self, expense_id: int):
        with sqlite3.connect(self.path) as conn:
            conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()

import flet as ft
from database import Database

def main(page: ft.Page):
    page.title = "Приложение учёта расходов"
    page.data = 0.0

    # создаем экземпляр класса Database
    db = Database("db.sqlite3")
    # создаем таблицы
    db.create_tables()

    def add_expense(e):
        expense = f"{name_input.value}, сумма: {amount_input.value} сом"
        print(expense)
        expense_list.controls.append(ft.Text(value=expense, size=30))
        page.data += float(amount_input.value)
        name_input.value = ""
        amount_input.value = ""
        total_text.value = f"Общая сумма: {page.data} сом"
        page.update()

    title = ft.Text(value="Учёт расходов", size=33)
    name_input = ft.TextField(label="Название расхода")
    amount_input = ft.TextField(label="Сумма расхода")
    add_button = ft.ElevatedButton("Добавить", on_click=add_expense)
    total_text = ft.Text(value=f"Общая сумма: {page.data} сом", size=28)
    expense_list = ft.Column()

    page.add(
        title,
        name_input,
        amount_input,
        add_button,
        total_text,
        expense_list
    )

ft.app(main)
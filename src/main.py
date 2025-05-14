import flet as ft

def main(page: ft.Page):
    page.title = "Приложение учёта расходов"

    title = ft.Text(value="Учёт расходов", size=30)
    name_input = ft.TextField(label="Название расхода")
    amount_input = ft.TextField(label="Сумма расхода")
    button = ft.ElevatedButton("Добавить")

    page.add(title, name_input, amount_input, button)

ft.app(target=main)

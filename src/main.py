import flet as ft
from database import Database

def main(page: ft.Page):
    page.title = "Приложение учёта расходов"
    page.data = 0.0

    db = Database("db.sqlite3")
    db.create_tables()

    title = ft.Text(value="Учёт расходов", size=33)
    name_input = ft.TextField(label="Название расхода")
    amount_input = ft.TextField(label="Сумма расхода")
    add_button = ft.ElevatedButton("Добавить")
    total_text = ft.Text(value=f"Общая сумма: {page.data} сом", size=28)
    expense_list_area = ft.Column()
    form_area = ft.Row(controls=[name_input, amount_input, add_button])

    def add_expense(e):
        name = name_input.value.strip()
        amount = float(amount_input.value.strip())

        if not name:
            return

        db.add_expense(name=name, amount=amount)

        expense_list_area.controls.clear()
        page.data = 0.0

        expenses = db.all_expenses()
        for exp in expenses:
            expense_list_area.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(value=f"Расход: {exp[1]}", size=30),
                        ft.Text(value=f"Сумма: {exp[2]} сом", size=30),
                    ]
                )
            )
            page.data += exp[2]

        name_input.value = ""
        amount_input.value = ""
        total_text.value = f"Общая сумма: {page.data} сом"
        page.update()

    add_button.on_click = add_expense

    page.add(
        title,
        form_area,
        total_text,
        expense_list_area
    )

    expenses = db.all_expenses()
    for exp in expenses:
        expense_list_area.controls.append(
            ft.Row(
                controls=[
                    ft.Text(value=f"Расход: {exp[1]}", size=30),
                    ft.Text(value=f"Сумма: {exp[2]} сом", size=30),
                ]
            )
        )
        page.data += exp[2]

    total_text.value = f"Общая сумма: {page.data} сом"
    page.update()

ft.app(target=main)

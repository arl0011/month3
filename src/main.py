import flet as ft
from database import Database


def main(page: ft.Page):
    page.title = "Приложение для учёта расходов"
    page.window.width = 1024

    db = Database("db.sqlite3")
    db.create_tables()

    expenses = db.all_expenses()
    print(expenses)

    def get_rows() -> list[ft.Row]:
        rows = []
        for expense in db.all_expenses():
            rows.append(
                ft.Row(
                    controls=[
                        ft.Text(value=expense[0]),
                        ft.Text(value=f"Название: {expense[1]}", size=30),
                        ft.Text(value=f"Сумма: {expense[2]} сом", size=30, color=ft.Colors.BLUE),
                        ft.IconButton(
                            icon=ft.Icons.EDIT,
                            icon_color=ft.Colors.GREEN,
                            icon_size=20,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color=ft.Colors.RED,
                            icon_size=20,
                            on_click=delete_expense,
                            data=expense[0],
                        ),
                    ]
                )
            )
        return rows

    def add_expense(e):
        db.add_expense(name=name_input.value, amount=float(amount_input.value))
        expense_list_area.controls = get_rows()
        name_input.value = ""
        amount_input.value = ""
        expense_count_text.value = f"Всего {db.count_expenses()} расходов"
        page.update()

    def delete_expense(e):
        print(f"В delete_expense нажали на расход с id={e.control.data}")
        db.delete_expense(expense_id=e.control.data)
        expense_list_area.controls = get_rows()
        expense_count_text.value = f"Всего {db.count_expenses()} расходов"
        page.update()

    title = ft.Text(value="Учёт расходов", size=33)
    name_input = ft.TextField(label="Название расхода")
    amount_input = ft.TextField(label="Сумма расхода")
    add_button = ft.ElevatedButton("Добавить", on_click=add_expense)
    expense_count_text = ft.Text(
        value=f"Всего {db.count_expenses()} расходов", size=28, color=ft.Colors.PINK
    )
    expense_list_area = ft.Column(controls=get_rows(), scroll="auto", expand=True)
    form_area = ft.Row(controls=[name_input, amount_input, add_button])
    title.value = "Приложение для учёта расходов"

    page.add(
        title,
        form_area,
        expense_count_text,
        expense_list_area,
    )


ft.app(main)

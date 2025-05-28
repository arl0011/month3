import flet as ft
from database import Database

def main(page: ft.Page):
    page.title = "Приложение для учёта расходов"
    page.window.width = 1024
    page.data = 0  # id расхода для редактирования

    db = Database("db.sqlite3")
    db.create_tables()

    def get_rows() -> list[ft.Row]:
        rows = []
        for expense in db.all_expenses():
            rows.append(
                ft.Row(
                    controls=[
                        ft.Text(value=str(expense[0])),
                        ft.Text(value=f"Название: {expense[1]}", size=30),
                        ft.Text(value=f"Сумма: {expense[2]} сом", size=30, color=ft.Colors.BLUE),
                        ft.IconButton(
                            icon=ft.Icons.EDIT_NOTE,
                            icon_color=ft.Colors.GREEN,
                            icon_size=20,
                            on_click=open_edit_modal,
                            data=expense[0],
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
        name_input.value = ""
        amount_input.value = ""
        expense_list_area.controls = get_rows()
        expense_count_text.value = f"Всего {db.count_expenses()} расходов"
        page.update()

    def delete_expense(e):
        db.delete_expense(expense_id=e.control.data)
        expense_list_area.controls = get_rows()
        expense_count_text.value = f"Всего {db.count_expenses()} расходов"
        page.update()

    def open_edit_modal(e):
        page.data = e.control.data
        expense = db.get_expense(expense_id=page.data)
        name_input.value = expense[1]
        amount_input.value = str(expense[2])
        page.dialog = edit_modal
        page.dialog.open = True
        page.update()

    def close_edit_modal(e):
        page.dialog.open = False
        page.update()

    def update_expense(e):
        db.update_expense(
            expense_id=page.data,
            name=name_input.value,
            amount=float(amount_input.value),
        )
        name_input.value = ""
        amount_input.value = ""
        expense_list_area.controls = get_rows()
        expense_count_text.value = f"Всего {db.count_expenses()} расходов"
        page.dialog.open = False
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

    edit_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Редактировать расход"),
        content=ft.Column(
            controls=[name_input, amount_input]
        ),
        actions=[
            ft.ElevatedButton("Сохранить", on_click=update_expense, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
            ft.ElevatedButton("Отменить", on_click=close_edit_modal),
        ],
    )

    page.add(title, form_area, expense_count_text, expense_list_area)

ft.app(target=main)

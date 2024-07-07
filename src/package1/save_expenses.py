from package1 import Expenses

from rich import print
from rich.console import Console
from rich.theme import Theme

console = Console()
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)


def save_expense(new_expense_object: Expenses, file_path):
    error.print(
        f"Saving your expense.... {new_expense_object} to {file_path}", style="success")
    with open(file_path, "a+") as f:
        f.write(f"{new_expense_object.name}, {new_expense_object.amount:.2f}, {new_expense_object.date}, {new_expense_object.category}\n")

# Import class Expenses from package 1 for use in code
from package1 import Expenses

# Install and import rich library for use in code
from rich import print
from rich.console import Console
from rich.theme import Theme

# Initialise console variable to use Rich Package installed from Pip
console = Console()

# Apply Theme colour to display success or error messages and initialise this to error for use as "error.print"
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)

# Define save expenses function
def save_expense(new_expense_object: Expenses, file_path):
    error.print(
        f"Saving your expense.... {new_expense_object} to {file_path}", style="success")
    with open(file_path, "a+") as f:
        f.write(f"{new_expense_object.name}, {new_expense_object.amount:.2f}, {new_expense_object.date}, {new_expense_object.category}\n")

from package3 import exit_program

import os.path
from rich import print
from rich.console import Console
from rich.theme import Theme

console = Console()
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)

def view_expenses(file_path):
    if os.path.exists(file_path):
        checkfile = os.stat(file_path).st_size
        while True:
            if checkfile == 0:
                error.print(
                "You do not have any expenses to remove", style="error")
                break
            else:
                view_expense = input(
                    "Would you like to view your expense entries? (yes/no): ")
                if view_expense.lower() == "yes":
                    with open("expenses_list.csv", "r") as f:
                        expense_list = f.readlines()
                        for i, expense in enumerate(expense_list):
                            print(f"{i+1}. {expense}".strip())

                        exit_program()
                        return

                elif view_expense.lower() == "no":
                    error.print(
                        "You have selected not to view your entries!", style="error")
                    return

                else:
                    error.print("Please enter a valid answer", style="error")
                    continue
    else:
        error.print("You currently have no expense entries", style="error")
        return

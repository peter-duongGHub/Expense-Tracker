# Import function exit_program from package3 for use
from package3 import exit_program

# Import os module and install rich library to use in code
import os.path
from rich import print
from rich.console import Console
from rich.theme import Theme

# Initialise console variable to use Rich Package installed from Pip
console = Console()

# Apply Theme colour to display success or error messages and initialise this to error for use as "error.print"
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)

# Define view expenses function
def view_expenses(file_path):
    # Using os module check file exists
    if os.path.exists(file_path):
        # Check contents of file
        checkfile = os.stat(file_path).st_size
        # While True loop to ensure file size is not 0 and user enters correct input
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
    #Else statement terminal output error message if file doesnt exist 
    else:
        error.print("You currently have no expense entries", style="error")
        return

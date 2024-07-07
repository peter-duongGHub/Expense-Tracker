# Import function exit_program from package3 and use it
from package3 import exit_program

# Import module os and import rich library for use in code
from rich.console import Console
from rich.theme import Theme
import os.path

# # Initialise console variable to use Rich Package installed from Pip
console = Console()

# Apply Theme colour to display success or error messages and initialise this to error for use as "error.print"
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)

# Define function total expenses


def total_expenses(file_path, user_budget, Expenses):
    # Use if condition to check if file path exists to continue
    if os.path.exists(file_path):
        # Initialise expenses list
        expenses: list[Expenses] = []
        # File I/O read file and initialise every line into variable lines
        with open(file_path, 'r') as f:
            lines = f.readlines()
            # For loop iterate each line in lines
            for line in lines:
                expense_name, expense_amount, expense_date, expense_category = line.strip().split(",")
                total_expense_object = Expenses(name=expense_name, amount=float(
                    expense_amount), date=expense_date, category=expense_category)
                expenses.append(total_expense_object)
            # Initialise amount by category dictionary
            amount_by_category = {}
            # For loop to iterate expense in expenses list previously created
            for expense in expenses:
                key = expense.category
                if key in amount_by_category:
                    amount_by_category[key] += expense.amount
                else:
                    amount_by_category[key] = expense.amount
            # For loop to iterate over each key, value pair in amount by category dictionary
            for key, value in amount_by_category.items():
                error.print(f"\n   {key} ${value:.2f}", style="success")

            # Sum total expenses as a net total iterating over each expense.amount
            spending_total = sum([expense.amount for expense in expenses])
            error.print(
                f"\nYou have spent a total of: ${spending_total:.2f}", style="success")
            # Display total budget after subtracting net total from user budget
            remaining_budget = user_budget - spending_total
            error.print(
                f"    Your remaining budget: ${remaining_budget:.2f}", style="success")
            # Prompt user to add another expense
            exit_program()
# If file doesnt exist terminal output error message and return to sub menu
    else:
        error.print("You have no expense entries to sum", style="error")
        return

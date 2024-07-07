# Import rich library and datetime module for use in code
from rich import print
import datetime
from rich.console import Console
from rich.theme import Theme


# Initialise console variable to use Rich Package installed from Pip
console = Console()

# Apply Theme colour to display success or error messages and initialise this to error for use as "error.print"
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)

# Create Class Expenses 
class Expenses:
    def __init__(self, name, amount, date, category):
        self.name = name
        self.amount = amount
        self.date = date
        self.category = category
    # Return as string for use in functions
    def __repr__(self):
        return f"{self.name}, {self.amount:.2f}, {self.date}, {self.category}"

# Define Add expense category
def add_expense_category(expense_name, expense_amount, expense_date):
    categories_expense = [
        "Food",
        "Bills",
        "Rent",
        "Car",
        "Education",
        "Miscellaneous"
    ]

    while True:
        try:
            console.print(
                "[bold yellow]Select a category from the following options: [/]")
            for i, category in enumerate(categories_expense):
                error.print(f"{i + 1}. {category}", style="success")

            user_select = int(input("Your chosen category number? "))

            if user_select not in range(1, (len(categories_expense) + 1)):
                error.print("Please select a valid category number: ",
                            style="error")
                continue

            else:
                error.print(
                    f"You have selected {user_select}: {categories_expense[user_select - 1]} ", style="success")
                category_selection = categories_expense[(user_select) - 1]
                new_expense_object = Expenses(
                    name=expense_name, amount=expense_amount, category=category_selection, date=expense_date)
                return new_expense_object
        except TypeError as e:
            print(f"Please enter an integer value (1-6): {e}", style="error")
            continue
        except Exception as e:
            error.print(
                f"Please enter an integer value (1-6): {e}", style="error")
            continue

# Define Add expense date
def add_expense_date():
    while True:
        try:
            expense_date = (
                input("Please enter a date in format YYYY-MM-DD: "))
            if datetime.date.fromisoformat(expense_date):
                error.print(
                    f"You have entered {expense_date}", style="success")
                return expense_date
            else:
                error.print(
                    "Invalid date entered, please enter a valid date!", style="error")
                continue

        except Exception as e:
            error.print(
                f"Invalid date entered, please enter a valid date!", style="error")
            continue

# Define Add expense name
def add_expense_name():
    while True:
        try:
            expense_name = input("Please enter an expense name: ")
            if expense_name.isalpha() and (20 >= len(expense_name) > 0):
                error.print(
                    f"You have entered {expense_name}", style="success")
                expense_name = expense_name.capitalize()
                return expense_name
            else:
                error.print(
                    f"Invalid input. Please enter a valid name including only letters!", style="error")
                continue

        except Exception as e:
            error.print(
                f"Invalid input. Please enter a valid name including only letters!: {e}", style="error")
            continue

# Define Add budget
def add_budget():
    while True:
        try:
            user_budget = float(input("Enter your budget: "))
            if user_budget <= 0:
                error.print("\nPlease enter a valid number\n", style="error")
                continue
            elif user_budget > 0:
                error.print(
                    f"Your budget is ${user_budget:.2f}", style="success")
                return user_budget
        except ValueError as e:
            error.print(f"Please enter a valid input: {e}\n", style="error")
            continue
        except Exception as e:
            print(f"Please enter a valid input: {e}", style="error")
            continue

# Define Add expense amount
def add_expense_amount():
    while True:
        try:
            expense_amount = float(input("Please enter an expense amount: "))
            if expense_amount <= 0:
                error.print(
                    "You cannot have an expense amount 0 or lower Please try again: ", style="error")
                continue
            elif expense_amount > 0:
                error.print(
                    f"You have entered {expense_amount:.2f}", style="success")
                return expense_amount
        except ValueError as e:
            error.print(
                f"\nPlease enter an integer value greater than 0: {e}\n ", style="error")
            continue
        except Exception as e:
            error.print(
                f"\nPlease enter an integer value greater than 0: {e}\n ", style="error")
            continue

from package3 import exit_program

from rich.console import Console
from rich.theme import Theme
import os.path


console = Console()
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)


def total_expenses(file_path, user_budget, Expenses):
    if os.path.exists(file_path):
        expenses: list[Expenses] = []
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                expense_name, expense_amount, expense_date, expense_category = line.strip().split(",")
                total_expense_object = Expenses(name=expense_name, amount=float(
                    expense_amount), date=expense_date, category=expense_category)
                expenses.append(total_expense_object)

            amount_by_category = {}
            for expense in expenses:
                key = expense.category
                if key in amount_by_category:
                    amount_by_category[key] += expense.amount
                else:
                    amount_by_category[key] = expense.amount

            for key, value in amount_by_category.items():
                error.print(f"\n   {key} ${value:.2f}", style="success")

            spending_total = sum([expense.amount for expense in expenses])
            error.print(
                f"\nYou have spent a total of: ${spending_total:.2f}", style="success")

            remaining_budget = user_budget - spending_total
            error.print(
                f"    Your remaining budget: ${remaining_budget:.2f}", style="success")

            exit_program()

    else:
        error.print("You have no expense entries to sum", style="error")
        return

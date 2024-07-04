from expenses import ExpenseTracker
from rich import print
from rich.console import Console
from rich.theme import Theme
from expenses import add_expense_amount, add_expense_category, add_expense_date, add_expense_name, save_expense, total_expenses, remove_expense, view_expenses, exit_program, main_menu

# Initialise
console = Console()
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)


def main():

    user_selection = main_menu()
    sub_menu(user_selection)


def sub_menu(user_selection):
    expense_file_path = "expenses_list.csv"
    if user_selection == 1:
        console.print("Starting your Expense Tracking Journey...",
                      style="bold underline yellow")
        while True:
            user_budget = float(input("Please enter your budget: "))
            if user_budget <= 0:
                error.print("\nPlease enter a valid number\n", style="error")
                continue
            else:
                error.print(
                    f"Your budget is ${user_budget:.2f}", style="success")
                break

        while True:
            console.print(
                "[bold dark_goldenrod]What would you like to do first?[/]\n")
            console.print("[bold underline orange_red1]Menu:[/] ")
            print("1.", ":pencil:",
                  "[bold green]Add[/] & [bold cornflower_blue]Save[/] Expense to Text File")
            print("2.", ":scroll:",
                  "[bold medium_purple]View[/] Expense Entries")
            print("3.", ":recycle:", " [bold red]Remove[/] an Expense")
            print("4.", ":heavy_plus_sign:", "[bold yellow2]Total[/] Expenses")
            print("5.", ":runner:",
                  "[bold bright_magenta]Return[/] to main menu\n")
            sub_selection = int(input("Make a choice (1-5): "))
            if sub_selection == 1:
                expense_name = add_expense_name()
                expense_amount = add_expense_amount()
                expense_date = add_expense_date()
                new_expense_object = add_expense_category(
                    expense_name, expense_amount, expense_date)
                save_expense(new_expense_object, expense_file_path)
                exit_program()
            elif sub_selection == 2:
                view_expenses(expense_file_path)
            elif sub_selection == 3:
                remove_expense(expense_file_path)
            elif sub_selection == 4:
                total_expenses(expense_file_path, user_budget)
            elif sub_selection == 5:
                print("-------------")
                main()
                return
            else:
                error.print("Please select a number between (1-5)",
                            style="error")

if __name__ == "__main__":
    main()

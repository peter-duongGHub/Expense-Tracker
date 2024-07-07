# Import Packages 1, 2 & 3 as well as Rich Package. Total = 4 Packages. Use each function from each package.
from package1 import add_budget, add_expense_amount, add_expense_name, add_expense_date, add_expense_category, save_expense, Expenses
from package2 import remove_expense, view_expenses
from package3 import main_menu, total_expenses, exit_program

from rich import print
from rich.console import Console
from rich.theme import Theme

# Initialise console variable to use Rich Package installed from Pip
console = Console()

# Apply Theme colour to display success or error messages and initialise this to error for use as "error.print"
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)

# Define the main function
def main():
    # Initialise returned value from main menu followed by running sub menu function
    user_selection = main_menu()
    sub_menu(user_selection)

# Define the sub menu function
def sub_menu(user_selection):
    # Initialise variable expense file path to a CSV file named "expenses_list.csv"
    expense_file_path = "expenses_list.csv"
    # If conditional statement to check user input meets certain value
    if user_selection == 1:
        # Terminal Output if user selection is equal to 1 
        console.print("Starting your Expense Tracking Journey...",
                      style="bold underline yellow")
        user_budget = add_budget()
        # Add while True loop to continue prompt if user enters invalid input
        while True:
            # Try block 
            try:
                # Print list of options to show user
                console.print(
                    "[bold dark_goldenrod]What would you like to do first?[/]\n")
                console.print("[bold underline orange_red1]Menu:[/] ")
                print("1.", ":pencil:",
                      "[bold green]Add[/] & [bold cornflower_blue]Save[/] Expense to CSV File")
                print("2.", ":scroll:",
                      "[bold medium_purple]View[/] Expense Entries")
                print("3.", ":recycle:", " [bold red]Remove[/] an Expense")
                print("4.", ":heavy_plus_sign:",
                      "[bold yellow2]Total[/] Expenses")
                print("5.", ":runner:",
                      "[bold bright_magenta]Return[/] to main menu\n")
                # Initialise variable to users integer selection
                sub_selection = int(input("Make a choice (1-5): "))
                # Selecting option 1 from sub menu will prompt adding an expense
                if sub_selection == 1:
                    expense_name = add_expense_name()
                    expense_amount = add_expense_amount()
                    expense_date = add_expense_date()
                    new_expense_object = add_expense_category(
                        expense_name, expense_amount, expense_date)
                    save_expense(new_expense_object, expense_file_path)
                    exit_program()
                # Selecting option 2 from sub menu will prompt viewing an expense
                elif sub_selection == 2:
                    view_expenses(expense_file_path)
                # Selecting option 3 from sub menu will prompt removing an expense
                elif sub_selection == 3:
                    remove_expense(expense_file_path)
                # Selecting option 4 from sub menu will prompt totalling expenses
                elif sub_selection == 4:
                    total_expenses(expense_file_path, user_budget, Expenses)
                # Selecting option 5 will return the user back to the main menu
                elif sub_selection == 5:
                    print("-------------")
                    main()
                    return
                # Error handling, if user enters invalid input terminal outputs an error message
                else:
                    error.print("Please select a number between (1-5)",
                                style="error")
                    continue
            # Except block for error handling, if user enters invalid input terminal outputs an error message
            except ValueError as e:
                error.print(
                    f"Please enter a valid item from the sub menu: {e}", style="error")
                continue

# Allows execution of code when running as script but not when imported as module
if __name__ == "__main__":
    main()

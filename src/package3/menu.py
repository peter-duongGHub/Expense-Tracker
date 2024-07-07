# Install library rich and import for use in code
from rich.console import Console
from rich.theme import Theme

# # Initialise console variable to use Rich Package installed from Pip
console = Console()

# Apply Theme colour to display success or error messages and initialise this to error for use as "error.print"
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)

# Define main menu function


def main_menu():
    while True:
        try:
            console.print(
                "\n:sunglasses:", "[bold cyan]Welcome to [green]Peter's Expense Tracker[/], track your expenses on the go![/]", ":bar_chart:")
            console.print(
                "[bold yellow]Choose from the following options (1-2):[/]", ":1234:")
            console.print("\n""1.", ":arrow_forward:",
                          "[bold green]Start[/] Expense Tracker")
            console.print("2.", ":door:", "[bold red]Exit[/] Program\n")
            user_selection = int(input("Make a selection: "))
            if user_selection == 1:
                return user_selection
            if user_selection == 2:
                console.print(
                    "[bold cyan]Thankyou for trying out [green]Peter's Expense Tracker[/], till next time![/]")
                break
            else:
                error.print("Please enter a valid number (1 or 2)",
                            style="error")

        except ValueError as e:
            error.print(
                f"Please enter a valid number (1 or 2): {e}", style="error")

        except Exception as e:
            error.print(
                f"Please enter a valid number (1 or 2): {e}", style="error")

# Define exit program function


def exit_program():
    # While True loop in case user enters wrong input
    while True:
        # Try block for error handling
        try:
            reprompt = input("Would you like to add more expenses? (yes/no): ")
            if reprompt.lower() == "yes" or reprompt.lower() == "no":
                return
            # Error handling, terminal output if wrong user input
            else:
                error.print("Please input either yes or no", style="error")
        # Except block for error handling
        except Exception as e:
            error.print(f"Please enter a valid input (yes/no): {e}")

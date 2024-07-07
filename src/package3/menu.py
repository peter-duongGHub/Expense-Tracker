from rich.console import Console
from rich.theme import Theme

console = Console()
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)

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
            


def exit_program():
    while True:
        try:
            reprompt = input("Would you like to add more expenses? (yes/no): ")
            if reprompt.lower() == "yes" or reprompt.lower() == "no":
                return
            else:
                error.print("Please input either yes or no", style="error")

        except Exception as e:
            error.print(f"Please enter a valid input (yes/no): {e}")
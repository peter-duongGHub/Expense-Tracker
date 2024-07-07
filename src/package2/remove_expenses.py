# Import os module from Python standard library and rich library for use in code
import os.path
from rich import print
from rich.console import Console
from rich.theme import Theme

# Initialise console variable to use Rich Package installed from Pip
console = Console()

# Apply Theme colour to display success or error messages and initialise this to error for use as "error.print"
custom_theme = Theme({"success": "green", "error": "red"})
error = Console(theme=custom_theme)

# Define remove expenses function
def remove_expense(file_path):
    while True:
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    checkfile = os.stat(file_path).st_size
                    if checkfile == 0:
                        error.print(
                            "You do not have any expenses to remove", style="error")
                        break
                    else:
                        for i, line in enumerate(lines):
                            print(f"{i+1}. {line}".strip())
                        user_delete = int(
                            input(f"\nWhich expense entry would you like to delete? (1 - {len(lines)}): "))
                        if not 1 <= user_delete <= len(lines):
                            print(
                                f"Enter valid option between 1 - {len(lines)}\n")
                            continue
                        else:
                            with open(file_path, 'w') as f:
                                index = 1
                                for line in lines:
                                    if index != user_delete:
                                        f.write(line)
                                    else:
                                        error.print(
                                            f"You have successfully deleted entry {user_delete}", style="success")

                                    index += 1

                            return

            else:
                error.print(
                    "You do not currently have any expense entries to remove! ", style="error")
                break

        except ValueError as e:
            error.print(
                f"Please enter a valid expense entry: {e}", style="error")
            continue
        except Exception as e:
            error.print(
                f"Please enter a valid expense entry: {e}", style="error")
            continue

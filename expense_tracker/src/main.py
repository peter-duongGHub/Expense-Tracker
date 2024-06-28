from expenses import ExpenseTracker
import datetime
import json



def main():
    print("Welcome to Peter's Expense Tracker")
    expense_file_list = "list_of_expenses.txt"

    # Get user input for Expense(s) including: Name, Amount, Category, Location, Date
    expense = get_user_input()
    
    # Append the expense to a file
    with open(expense_file_list, "a") as f:
        f.write(f"\n{expense}")

    # Read list of total expenses
    with open(expense_file_list, "r") as f:
        read_list = f.read()
        if len(expense_file_list) == 0:
            print("Nothing in list")
        else:
            print(f"Here are a list of your expenses{read_list}")


    # Remove files


    # if __name__ == "__main__":
    #     main()
   
def get_user_input():

    expense_name = input("Please enter an expense name: ")
    if expense_name.isalpha() and (20 >= len(expense_name) > 0):
        print(f"You have entered {expense_name}")
        expense_name = expense_name.capitalize()
    else:
        print("Please type a valid name") 

    expense_amount = float(input("Please enter an expense amount: "))
        
    if expense_amount == 0:
        print("You cannot have an expense of 0 amount! Please try again: ")
    else:
        print(f"You have entered {expense_amount:.2f}")

        expense_location = input("Please enter location of expense: ")
        expense_location = expense_location.upper()
        if not expense_location.isalpha():
            print("Please enter a valid location: ")
        else:
            print(f"You have entered {expense_location}")

        expense_date = (input("Please enter a date in format YYYY-MM-DD: "))
        if datetime.date.fromisoformat(expense_date):
            print(f"You have entered {expense_date}")
        else:
            ("Invalid date entered, please enter a valid date!")

        categories_expense = [
        "Food", 
        "Bills", 
        "Rent", 
        "Car", 
        "Education", 
        "Miscellaneous"
            ]
        
        
    while True:
        print("Select a category from the following options: ")
        for i, category in enumerate(categories_expense):
            print(f"{i + 1}. {category}")
        user_select = int(input("Your chosen category number: "))

        if user_select not in range(1, (len(categories_expense) + 1)):
            print("Please select a valid category number: ")
            continue
            
        else:
            print(f"You have selected {user_select}: {categories_expense[user_select - 1]} ")
            category_selection = categories_expense[(user_select) - 1]
            new_expense_object = ExpenseTracker(name=expense_name, amount=expense_amount, category=category_selection, location=expense_location, date=expense_date
                )
            return new_expense_object
            

        # expense_location = input("Please enter location details: ")
        # expense_time = input("Please enter the time when expense occured: ")
main()

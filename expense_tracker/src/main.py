from expenses import ExpenseTracker
import datetime
import json



def main():
    print("Welcome to Peter's Expense Tracker")

    print("What would you like to do first?: ")
    print("1. Add Expense(s)")
    print("2. View Expense(s)")
    print("3. Remove Expense(s)")
    print("4. Exit Program")

    while True:
        user_selection = int(input("Your selection option please: "))
        if user_selection in range(1, 5):
            if user_selection == 1:
                get_user_input()
            elif user_selection == 2:
                if len(view_expense()) != 0:
                    for row in view_expense():
                        print(row.strip())
                else:
                    print("Nothing in list")
                    
            elif user_selection == 3:
                x = view_expense()

                if len(x) == 0:
                    print("There are no expenses to remove! ")
                else:
                    remove_expense(x)
                            
            return
        
        else:
            print("Invalid Option, please try again! ")


        expense_file_list = "list_of_expenses.txt"


    # Get user input for Expense(s) including: Name, Amount, Category, Location, Date    
    # Append the expense to a file


    # Read list of total expenses
    
def view_expense():
    with open("list_of_expenses.txt", "r") as f:
        read_list = f.readlines()
        return read_list

    # Remove files


    # if __name__ == "__main__":
    #     main()

def remove_expense(x):
    print("Here are a list of your expenses: ")
    for expenseindex, expenseitems in enumerate(x):
        print(f"{expenseindex + 1}. {expenseitems}".strip())
        remove_selection = int(input("Which expense would you like to remove? "))
        with open("list_of_expenses.txt", 'w') as f:
            for i, line in enumerate(x):
                if i in [remove_selection]:
                    f.write(line)
                    return


   
def get_user_input():
    count = 0
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
        user_select = int(input("Your chosen category number? "))

        if user_select not in range(1, (len(categories_expense) + 1)):
            print("Please select a valid category number: ")
            continue
            
        else:
            print(f"You have selected {user_select}: {categories_expense[user_select - 1]} ")
            category_selection = categories_expense[(user_select) - 1]
            new_expense_object = ExpenseTracker(name=expense_name, amount=expense_amount, category=category_selection, location=expense_location, date=expense_date
                )
            count += 1
            with open("list_of_expenses.txt", "a") as f:
                f.write(f"{new_expense_object}\n")
            return new_expense_object, count
            
main()

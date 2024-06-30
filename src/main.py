from expenses import ExpenseTracker
import datetime
import json
import re
import os.path



def main():
    
    
    main_menu()

    sub_menu()





    # Get user input for Expense(s) including: Name, Amount, Category, Location, Date    
    # Append the expense to a file


    # Read list of total expenses

def sub_menu():
    expense_file_path = "expenses_list.csv"
    
    while True:
        user_selection = int(input("Your selection option please: "))
        if user_selection in range(1, 7):
            if user_selection == 1:
                print("Starting your Expense Tracking Journey...")
                user_budget = float(input("Please enter your budget: "))
                print(f"Your budget is ${user_budget:.2f}")
                print("What would you like to do first?\n")
                print("Menu: ")
                print("1. Add & Save Expense to Text File")
                print("2. View Expense Entries")
                print("3. Remove an Expense")
                print("4. Total Expenses")
                print("5. Return to main menu\n")
            sub_selection = int(input("Make a choice (1-5): "))
            if sub_selection == 1:
                 add_expense(expense_file_path)
            elif sub_selection == 2:
                view_expenses(expense_file_path)   
            elif sub_selection == 3:
                remove_expense(expense_file_path)
            elif sub_selection == 4:
                total_expenses(expense_file_path, user_budget)
            elif sub_selection == 6:
                print("-------------")
                return f"{main_menu()}"

    

          
            return
        
        else:
            print("Invalid Option, please try again! ")


def main_menu():
    print("Welcome to Peter's Expense Tracker, track your expenses on the go!")
    print("Choose from the following options (1-4): ")
    print("1. Start Expense Tracker")
    print("2. Load existing Expenses")
    print("3. View Instructions")
    print("4. Exit Program\n")


def total_expenses(file_path, user_budget):
    expenses: list[ExpenseTracker] = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:  
            expense_name, expense_amount, expense_location, expense_date, expense_category = line.strip().split(",")
            total_expense_object = ExpenseTracker(name=expense_name,amount=float(expense_amount),location=expense_location,date=expense_date,category=expense_category)
            expenses.append(total_expense_object)

        amount_by_category = {}
        for expense in expenses:
            key = expense.category
            if key in amount_by_category:
                amount_by_category[key] += expense.amount
            else:
                amount_by_category[key] = expense.amount

        for key, value in amount_by_category.items():
            print(f"\n   {key} ${value:.2f}")
            
        
        spending_total = sum([x.amount for x in expenses])
        print(f"\nYou have spent a total of: ${spending_total:.2f}")

        remaining_budget = user_budget - spending_total
        print(f"    Your remaining budget: ${remaining_budget:.2f}")

    
def view_expenses(file_path):
    if os.path.exists(file_path):
        view_expense = input("Would you like to view your expense entries? (yes/no): ")
        if view_expense.isalpha() and view_expense.lower() == "yes":  
            with open("expenses_list.txt", "r") as f:
                listed_expense = f.readlines()
                for i, expense in enumerate(listed_expense):
                    print(f"{i+1}. {expense}".strip())
                return
        else:
            print("You have selected not to view your entries!")
    else: 
        print("You currently have no expense entries")

    

    # Remove files


    # if __name__ == "__main__":
    #     main()

def remove_expense(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                lines = f.readlines()
                view_expenses()
                delete_line = int(input("Which expense entry would you like to delete? "))
                lineindex = 1
                with open(file_path, 'w') as f:
                    for line in lines:
                        if lineindex != delete_line:
                            f.write(line)
                        lineindex += 1

            print(f"You have successfully deleted entry {delete_line}")

        else:
            print("You do not currently have any expense entries to remove! ")

def save_expense(new_expense_object:ExpenseTracker, file_path):
    print(f"Saving your expense.... {new_expense_object} to {file_path}")
    with open(file_path, "a+") as f:
        f.write(f"{new_expense_object.name}, {new_expense_object.amount:.2f}, {new_expense_object.location}, {new_expense_object.date}, {new_expense_object.category}\n")

def add_expense(file_path):
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
            
            save_expense(new_expense_object, file_path)
            
            return new_expense_object
            
main()
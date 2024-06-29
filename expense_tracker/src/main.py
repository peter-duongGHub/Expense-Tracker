from expenses import ExpenseTracker
import datetime
import json
import re
import os.path


def main():
    print("Welcome to Peter's Expense Tracker, track your expenses on the go!")

    print("Choose from the following options (1-4): ")
    print("1. Start Expense Tracker")
    print("2. Load existing Expenses")
    print("3. View Instructions")
    print("4. Exit Program\n")

    while True:
        user_selection = int(input("Your selection option please: "))
        if user_selection in range(1, 5):
            if user_selection == 1:
                print("Starting your Expense Tracking Journey...")
                print("What would you like to do first?\n")
                print("Menu: ")
                print("1. Add Income")
                print("2. View Income Entries")
                print("3. Add Expense")
                print("4. View Expense Entries")
                print("5. Remove an Expense")
                print("6. Return to main menu\n")
                sub_selection = int(input("Make a choice (1-7): "))
                if sub_selection == 1:
                    income_input = int(input("What is your income? "))
                    print(f"You have added income: ${add_income(income_input)}\n")
                elif sub_selection == 2:
                    view_income()
                elif sub_selection == 3:
                    get_user_input()
                elif sub_selection == 4:
                    view_expense()   
                elif sub_selection == 5:
                    remove_expense()

                    
          
            # elif user_selection == 3:
            #     x = view_expense()

            #     if len(x) == 0:
            #         print("There are no expenses to remove! ")
            #     else:
            #         remove_expense(x)
                            
            return
        
        else:
            print("Invalid Option, please try again! ")



    # Get user input for Expense(s) including: Name, Amount, Category, Location, Date    
    # Append the expense to a file


    # Read list of total expenses

def view_income():
    FILE_PATH = "./income_list.txt"
    if os.path.exists(FILE_PATH):
        view_income = input("Would you like to view your income entries? (yes/no): ")
        if view_income.isalpha() and view_income.lower() == "yes":  
            with open("income_list.txt", "r") as f:
                listed_income = f.readlines()
                for i, line in enumerate(listed_income):
                    print(f"{i+1}. {line}".strip())
                return listed_income
        else:
            print("You have selected not to view your entries!")
    else: 
        print("You currently have no income entries")

def add_income(input):
    income = 0
    income += input
    new_income = re.sub(r'(\d{3})(?=\d)' , r'\1,', str(income)[::-1])[::-1]
    
    with open("income_list.txt", 'a+') as f:
        f.write(f"${new_income}\n")

    return new_income
    
def view_expense():
    FILE_PATH = "./expense_list.txt"
    if os.path.exists(FILE_PATH):
        view_expense = input("Would you like to view your expense entries? (yes/no): ")
        if view_expense.isalpha() and view_expense.lower() == "yes":  
            with open("expense_list.txt", "r") as f:
                listed_expense = f.readlines()
                for i, expense in enumerate(listed_expense):
                    print(f"{i+1}. {expense}".strip())
                    return listed_expense
        else:
            print("You have selected not to view your entries!")
    else: 
        print("You currently have no expense entries")

    

    # Remove files


    # if __name__ == "__main__":
    #     main()

def remove_expense():
        FILE_PATH = "./expense_list.txt"
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'r') as f:
                lines = f.readlines()
                lineindex = 1
                view_expense()
                delete_line = int(input("Which expense entry would you like to delete? "))
                with open(FILE_PATH, 'w') as f:
                    for textline in lines:
                        if lineindex != delete_line:
                            f.write(textline)
                            lineindex+=1
                        else:
                            print(f"You have successfully deleted entry {delete_line}")

        else:
            print("You do not currently have any expense entries to remove! ")

        #     with open("expense_list.txt", 'r') as f:
        #         file_lines = f.readlines()
        #         for number, line in file_lines:
        #             print(f"Here are a list of your expenses: ")
        #             print(f"{number}. {line}")
        #     with open("expense_list.txt", "w") as f:
        #         delete_filename = int(input("Which expense would you like to remove? "))
        #         for i, items in file_lines:
        #             if i in [delete_filename]:
        #                 f.write(items)
        #             else:
        #                 print("Please enter a valid item")
        # else:
        #     print("You do not have any expenses to remove! ")
                

            
        


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
            with open("expense_list.txt", "a+") as f:
                f.write(f"{new_expense_object}\n")
            return new_expense_object, count
            
main()

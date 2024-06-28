from expenses import ExpenseTracker


def main():


    # print("Welcome to Peter's Expense Tracker! ")
    # print("Please enter your expense name: ")
    # print("Please enter your expense amount: ")
    # print("Please select a category from the following options: ")

    # print("\nExpense Tracker:")
    # print("1. Add Expense(s) ")
    # print("2. Remove Expense(s) ")
    # print("3. View Expense(s) ")
    # print("4. Edit Expense(s) ")
    # print("5. Total sum of Expense(s) ")
    # print("6. Save and Exit")
    expense = get_user_input()

# Get User Input (includes: name, amount, category, location, time)
    def get_user_input():

        expense_name = input("Please enter an expense name: ")
        if expense_name.isalpha() and (20 >= len(expense_name) > 0):
            print(f"You have entered {expense_name}")
        else:
            print("Please type a valid name") 

        expense_amount = float(input("Please enter an expense amount: "))
        
        if expense_amount == 0:
            print("You cannot have an expense of 0 amount! Please try again: ")
        else:
            print(f"You have entered {expense_amount:.2f}")
        
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
                print(f"You have selected {user_select}: {category[i]} ")
                new_expenses = ExpenseTracker()
                return

        expense_location = input("Please enter location of expense: ")



        expense_time = input("Please enter time of expense: ")


        # expense_location = input("Please enter location details: ")
        # expense_time = input("Please enter the time when expense occured: ")

    # if __name__ == "__main__":
    #     main()

    get_user_input()

main()
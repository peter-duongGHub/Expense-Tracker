class ExpenseTracker:
    def __init__(self, name, amount, location, date, category ):
        self.name = name
        self.amount = amount
        self.location = location
        self.date = date
        self.category = category

    def __repr__(self):
        return f"Expense: {self.name}, {self.category}, Location: {self.location} Amount: {self.amount:.2f} Date: {self.date}"


    # def given_name(self):
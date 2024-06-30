class ExpenseTracker:
    def __init__(self, name, amount, location, date, category ):
        self.name = name
        self.amount = amount
        self.location = location
        self.date = date
        self.category = category

    def __repr__(self):
        return f"<{self.name}, {self.amount:.2f}, {self.location}, {self.date}, {self.category}>"



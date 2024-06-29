class ExpenseTracker:
    def __init__(self, name, amount, location, date, category ):
        self.name = name
        self.amount = amount
        self.location = location
        self.date = date
        self.category = category

    def __repr__(self):
        return f"{self.name}, {self.category}, {self.location}, {self.amount:.2f}, {self.date}"



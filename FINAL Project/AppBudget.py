class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spends = []
    category_names = []

    # Step 1: Calculate total spent per category (withdrawals only)
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spends.append(total)
        category_names.append(category.name)

    total_spent = sum(spends)
    percentages = [(int((spend / total_spent) * 10) * 10) for spend in spends]  # rounded down to nearest 10

    # Step 2: Build the bar chart
    chart = ""
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Step 3: Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Step 4: Vertical category names
    max_len = max(len(name) for name in category_names)
    for i in range(max_len):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return title + chart.rstrip("\n")

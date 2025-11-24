def summary():
    try:
        with open("expenses.txt", "r") as f:
            data = f.readlines()

        if not data:
            print("No expenses found!")
            return

        total = 0
        category_dict = {}

        for line in data:
            date, category, amount = line.strip().split(",")
            amount = float(amount)
            total= total+ amount

            if category not in category_dict:
                category_dict[category] = 0
            category_dict[category] += amount

        print("\n===== EXPENSE SUMMARY =====")
        print(f"Total Expense: ₹{total}\n")

        print("Category Wise Breakdown:")
        for cat, amt in category_dict.items():
            print(f"{cat}: ₹{amt}")

    except FileNotFoundError:
        print("====No data found.====")
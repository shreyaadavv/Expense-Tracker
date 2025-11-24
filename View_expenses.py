def view():
    try:

        with open("expenses.txt", "r") as f:
           lines= f.readlines()
        expenses=[line.strip() for line in lines if line.strip()]
        if not expenses:
            print("\n -------No Expenses Found-------")
            return
        print("\n------***** All Expenses ****-------")
        for expense in expenses:
            print(expense)
        print("--------------------")
    except FileNotFoundError:
        print("\n ------------expense.txt file not found----------")

        
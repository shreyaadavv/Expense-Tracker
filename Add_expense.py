def add():
    date = input("Enter the date of spending : ")
    category = input("Enter a valid reason of spending : ")
    amount = input("Enter the amount spend : ")
    

    with open("expenses.txt", "a") as f:
        f.write(f"{date} | {category} | {amount}\n")

    print("Expense added successfully!")
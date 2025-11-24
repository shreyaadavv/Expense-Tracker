from Add_expense import add
from View_expenses import view
from Delete_expense import delete
from Expense_Summary import summary

def menu():
    print("\n ----****** EXPENSE TRACKER ******---- ")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Delete Expense")
    print("4. Expense Summary")
    print("5. Exit")

while True:
    menu()
    choice = int(input(" Enter your Choice : "))

    if choice == 1:
        add()

    elif choice == 2:
        view()

    elif choice == 3:
        delete()

    elif choice == 4:
        summary()

    elif choice == 5:
        print("-------EXITED-------")
        break

    else:
        print("====INVALID SYNTAX====")
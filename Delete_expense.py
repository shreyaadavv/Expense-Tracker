def delete():
    view = []
    try:
        with open("expenses.txt", "r") as f:
            view = f.readlines()

        if not view:
            print("No expenses to delete.")
            return

        for i, line in enumerate(view):
            print(f"{i+1}. {line.strip()}")

        num = int(input("Enter the expense number to delete: "))

        if 1 <= num <= len(view):
            removed = view.pop(num - 1)
            print("Deleted:", removed.strip())

            with open("expenses.txt", "w") as f:
                f.writelines(view)

        else:
            print("-------Invalid number!------")

    except FileNotFoundError:
        print("=====No data found.====")
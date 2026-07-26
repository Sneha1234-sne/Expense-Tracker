import os

FILE_NAME = "expenses.txt"

expenses = []


# -------------------------------
# Load Expenses from File
# -------------------------------
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expenses.append({
                    "category": category,
                    "amount": float(amount)
                })


# -------------------------------
# Save Expense
# -------------------------------
def save_expense(category, amount):
    with open(FILE_NAME, "a") as file:
        file.write(f"{category},{amount}\n")


# -------------------------------
# Add Expense
# -------------------------------
def add_expense():
    print("\nAvailable Categories")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Entertainment")
    print("5. Bills")
    print("6. Others")

    choice = input("Choose Category: ")

    category_dict = {
        "1": "Food",
        "2": "Travel",
        "3": "Shopping",
        "4": "Entertainment",
        "5": "Bills",
        "6": "Others"
    }

    category = category_dict.get(choice)

    if category is None:
        print("Invalid Category!")
        return

    try:
        amount = float(input("Enter Expense Amount: ₹"))

        expenses.append({
            "category": category,
            "amount": amount
        })

        save_expense(category, amount)

        print("Expense Added Successfully.")

    except:
        print("Invalid Amount!")


# -------------------------------
# View Expenses
# -------------------------------
def view_expenses():

    if len(expenses) == 0:
        print("\nNo Expenses Found!")
        return

    print("\n------ Expense History ------")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - ₹{expense['amount']}")


# -------------------------------
# Total Expense
# -------------------------------
def total_expense():

    total = sum(expense["amount"] for expense in expenses)

    print("\nTotal Expense = ₹", total)


# -------------------------------
# Category Summary
# -------------------------------
def category_summary():

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    print("\nCategory Wise Summary")

    for category, total in summary.items():
        print(category, ":", "₹", total)


# -------------------------------
# Search Expense
# -------------------------------
def search_expense():

    category = input("Enter Category Name: ").title()

    found = False

    print()

    for expense in expenses:
        if expense["category"] == category:
            print(category, "₹", expense["amount"])
            found = True

    if not found:
        print("No Expense Found.")


# -------------------------------
# Delete Expense
# -------------------------------
def delete_expense():

    view_expenses()

    if len(expenses) == 0:
        return

    try:
        index = int(input("\nEnter Expense Number to Delete: "))

        if 1 <= index <= len(expenses):

            expenses.pop(index - 1)

            with open(FILE_NAME, "w") as file:
                for expense in expenses:
                    file.write(
                        f"{expense['category']},{expense['amount']}\n")

            print("Expense Deleted Successfully.")

        else:
            print("Invalid Number.")

    except:
        print("Invalid Input.")


# -------------------------------
# Main Menu
# -------------------------------
load_expenses()

while True:

    print("\n==============================")
    print(" PROFESSIONAL EXPENSE TRACKER ")
    print("==============================")

    print("1. Add Expense")
    print("2. View Expense History")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Search Expense")
    print("6. Delete Expense")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        search_expense()

    elif choice == "6":
        delete_expense()

    elif choice == "7":
        print("\nThank You for using Expense Tracker!")
        break

    else:
        print("Invalid Choice!")
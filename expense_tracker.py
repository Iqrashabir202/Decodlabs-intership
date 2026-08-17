# DecodeLabs - Python Programming Project 2
# Expense Tracker

print("================================")
print("       EXPENSE TRACKER")
print("================================")

total = 0

while True:
    print("\nEnter an expense amount.")
    print("Enter 'done' when you have finished.")

    expense = input("Expense: ")

    # Stop entering expenses
    if expense.lower() == "done":
        break

    # Convert input into a number
    try:
        expense = float(expense)

        # Add expense to total
        total = total + expense

        print(f"Expense added: {expense:.2f}")
        print(f"Current total: {total:.2f}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Display final result
print("\n================================")
print("       EXPENSE SUMMARY")
print("================================")
print(f"Total Spent: {total:.2f}")
print("================================")
print("Thank you for using Expense Tracker!")

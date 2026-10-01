expenses = []

# Get expenses from the user
expense = float(input("Enter an expense or 0 to finish: "))

while expense != 0:
    if expense < 0:
        print("Expense cannot be negative.")
    else:
        expenses.append(expense)

    expense = float(input("Enter an expense or 0 to finish: "))

# Counters
small = 0
moderate = 0
large = 0

# Classify expenses
for expense in expenses:
    if expense < 25:
        small += 1
    elif expense <= 100:
        moderate += 1
    else:
        large += 1

# Calculate values
total = sum(expenses)
average = total / len(expenses)
smallest = min(expenses)
largest = max(expenses)

# Print results
print("\nExpense Summary")
print("---------------")
print(f"Number of expenses: {len(expenses)}")
print(f"Total: ${total:,.2f}")
print(f"Average: ${average:,.2f}")
print(f"Smallest expense: ${smallest:,.2f}")
print(f"Largest expense: ${largest:,.2f}")
print(f"Small expenses: {small}")
print(f"Moderate expenses: {moderate}")
print(f"Large expenses: {large}")
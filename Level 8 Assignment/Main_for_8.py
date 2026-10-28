from Level_8_Assignment import BankAccount

print("Welcome to the Bank!")

name = input("Please enter your name: ")
account = BankAccount(name)

# Deposit money
def make_deposit():
    amount = float(input("How much would you like to deposit? "))
    account.deposit(amount)

# Withdraw money
def make_withdraw():
    amount = float(input("How much would you like to withdraw? "))

    if account.withdraw(amount):
        print("Withdrawal Complete.")
    else:
        print("You do not have enough money.")

# Show account information
def view_account():
    account.show_info()


choice = ""

while choice != "4":
    print()
    print("Please choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        make_deposit()
    elif choice == "2":
        make_withdraw()
    elif choice == "3":
        view_account()
    elif choice == "4":
        print("Thank you for your business!")
    else:
        print("Invalid choice. Please try again.")
import re
import hashlib
from models.transaction import Transaction
from models.user import User

current_user = None

def validate_phone(phone):
    return re.match(r'^\d{10}$', phone)

def register_user():
    global current_user
    print("\nRegister User")
    name = input("Enter your name: ")
    phone = input("Enter your phone (10 digits): ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if not validate_phone(phone):
        print("Invalid phone number. It must be 10 digits.")
        return None

    user = User(name, phone, email, password)
    user.save()
    current_user = user
    print("Registration successful! You are now logged in.")
    return user

def sign_in_user():
    global current_user
    print("\nSign In")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = User.find_by_email(email)
    if user and user.check_password(password):
        current_user = user
        print("Sign in successful! You are now logged in.")
        return user
    else:
        print("Invalid email or password.")
        return None

def user_dashboard():
    while True:
        print("\nWelcome to your dashboard!")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("> ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def add_transaction():
    global current_user
    if not current_user:
        print("You need to log in first.")
        return

    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    trans_type = input("Enter type (income/expense): ").lower()

    transaction = Transaction(amount, date, category, description, trans_type, current_user.id)
    transaction.save()
    print("Transaction added successfully!")

def view_transactions():
    global current_user
    if not current_user:
        print("You need to log in first.")
        return

    print("\nView Transactions")
    print("1. View all transactions")
    print("2. Filter by date")
    print("3. Filter by category")
    print("4. Filter by type (income/expense)")
    print("5. Filter by type and category")
    choice = input("> ")

    if choice == "1":
        transactions = Transaction.all(current_user.id)
    elif choice == "2":
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        transactions = Transaction.filter_by_date(start_date, end_date, current_user.id)
    elif choice == "3":
        category = input("Enter category: ")
        transactions = Transaction.filter_by_category(category, current_user.id)
    elif choice == "4":
        trans_type = input("Enter type (income/expense): ").lower()
        transactions = Transaction.filter_by_type(trans_type, current_user.id)
    elif choice == "5":
        trans_type = input("Enter type (income/expense): ").lower()
        category = input("Enter category: ")
        transactions = Transaction.filter_by_type_and_category(trans_type, category, current_user.id)
    else:
        print("Invalid choice")
        return

    for trans in transactions:
        print(f"Amount: {trans.amount}, Date: {trans.date}, Category: {trans.category}, Description: {trans.description}, Type: {trans.trans_type}")

def generate_report():
    # Implement report generation logic here
    print("Report generation is not implemented yet.")

def exit_program():
    print("Exiting...")
    exit()

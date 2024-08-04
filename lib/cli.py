from helpers import (
    exit_program,
    add_transaction,
    view_transactions,
    generate_report,
    register_user,
    sign_in_user
)

current_user = None

def main():
    global current_user
    while True:
        if not current_user:
            auth_menu()
            choice = input("> ")
            if choice == "1":
                current_user = sign_in_user()
            elif choice == "2":
                current_user = register_user()
            elif choice == "0":
                exit_program()
            else:
                print("Invalid choice")
        else:
            user_dashboard()
            choice = input("> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                add_transaction()
            elif choice == "2":
                view_transactions()
            elif choice == "3":
                generate_report()
            else:
                print("Invalid choice")

def auth_menu():
    print("\nWelcome to the Personal Finance Tracker!")
    print("Please select an option:")
    print("1. Sign in")
    print("2. Register")
    print("0. Exit")

def user_dashboard():
    print("\nWelcome to your dashboard!")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Generate Report")
    print("4. Exit")

if __name__ == "__main__":
    main()

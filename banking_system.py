class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} has been deposited. New balance is {self.balance}.")
        else:
            print("Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} has been withdrawn. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Please enter a positive amount.")

    def check_balance(self):
        print(f"Your current balance is {self.balance}.")

def main():
    print("Welcome to the Python Bank!")
    account_name = input("Enter the account holder's name: ")
    account = BankAccount(account_name)

    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "4":
            print("Thank you for using Python Bank!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

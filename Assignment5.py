class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

def main():
    accounts = {}
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            if account_number in accounts:
                print("Account already exists.")
            else:
                accounts[account_number] = BankAccount(account_number, account_holder)
                print("Account created successfully.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            print("Exiting the banking system. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
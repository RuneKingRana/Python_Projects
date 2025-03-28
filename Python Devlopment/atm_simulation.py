class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")
        self.transaction_history.append("Checked balance")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ₹{amount}. New balance: ₹{self.balance}")
            self.transaction_history.append(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
            self.transaction_history.append(f"Withdrew ₹{amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin
            print("PIN successfully changed.")
            self.transaction_history.append("Changed PIN")
        else:
            print("Incorrect old PIN.")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


def main():
    pin = int(input("Set your ATM PIN: "))
    atm = ATM(pin)

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            entered_pin = int(input("Enter PIN: "))
            if atm.check_pin(entered_pin):
                atm.check_balance()
            else:
                print("Incorrect PIN.")

        elif choice == '2':
            entered_pin = int(input("Enter PIN: "))
            if atm.check_pin(entered_pin):
                amount = float(input("Enter deposit amount: "))
                atm.deposit(amount)
            else:
                print("Incorrect PIN.")

        elif choice == '3':
            entered_pin = int(input("Enter PIN: "))
            if atm.check_pin(entered_pin):
                amount = float(input("Enter withdrawal amount: "))
                atm.withdraw(amount)
            else:
                print("Incorrect PIN.")

        elif choice == '4':
            old_pin = int(input("Enter old PIN: "))
            new_pin = int(input("Enter new PIN: "))
            atm.change_pin(old_pin, new_pin)

        elif choice == '5':
            entered_pin = int(input("Enter PIN: "))
            if atm.check_pin(entered_pin):
                atm.show_transaction_history()
            else:
                print("Incorrect PIN.")

        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

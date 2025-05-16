import uuid
from datetime import datetime


class Transaction:
    def __init__(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {self.description}: ${self.amount:.2f}"


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.account_id = str(uuid.uuid4())[:8]
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(Transaction(amount, "Deposit"))
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.transactions.append(Transaction(-amount, "Withdrawal"))
        return self

    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transactions.append(Transaction(-amount, f"Transfer to {target_account.owner}"))
        her

    def show_transactions(self):
        for t in self.transactions:
            print(t)

    def __str__(self):
        return f"Account({self.account_id}) | Owner: {self.owner} | Balance: ${self.balance:.2f}"

    def __eq__(self, other):
        return self.account_id == other.account_id


class Bank:
    accounts = []

    @classmethod
    def create_account(cls, owner, balance=0):
        account = Account(owner, balance)
        cls.accounts.append(account)
        return account

    @classmethod
    def find_account(cls, account_id):
        for acc in cls.accounts:
            if acc.account_id == account_id:
                return acc
        raise LookupError("Account not found.")

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


# ================================
# 🧪 MAIN LOGIC TO TEST EVERYTHING
# ================================

def main():
    print("=== Creating accounts ===")
    amit = Bank.create_account("Amit", 1000)
    elon = Bank.create_account("Elon", 500)

    print(amit)
    print(elon)

    print("\n=== Deposit and Withdraw ===")
    amit.deposit(200).withdraw(150)
    print(amit)

    print("\n=== Transfer Funds ===")
    amit.transfer(elon, 300)
    print(amit)
    print(elon)

    print("\n=== Transactions for Amit ===")
    amit.show_transactions()

    print("\n=== Transactions for Elon ===")
    elon.show_transactions()

    print("\n=== Search Account ===")
    found = Bank.find_account(amit.account_id)
    print("Found:", found)

    print("\n=== Check Valid Amount ===")
    print("Is 50 valid?", Bank.is_valid_amount(50))
    print("Is -5 valid?", Bank.is_valid_amount(-5))

if __name__ == "__main__":
    main()

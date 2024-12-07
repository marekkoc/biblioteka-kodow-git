class BankAccount:
    def __init__(self, account_holder: str, balance: int = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    # Comparison based on account balance
    def __lt__(self, other: "BankAccount") -> bool:
        return self.balance < other.balance

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BankAccount):
            raise NotImplementedError
        return self.balance == other.balance


def main() -> None:
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob", 1500)

    print(account1 < account2)  # True, because Alice's balance is less than Bob's
    print(account1 == account2)  # False, because their balances are not equal


if __name__ == "__main__":
    main()

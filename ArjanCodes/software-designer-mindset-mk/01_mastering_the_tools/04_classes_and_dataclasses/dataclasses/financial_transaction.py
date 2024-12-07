from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class FinancialTransaction:
    transaction_id: str
    amount: int
    currency: str
    transaction_date: datetime
    description: Optional[str] = None


def main() -> None:
    transaction = FinancialTransaction(
        transaction_id="TXN12345",
        amount=999,
        currency="USD",
        transaction_date=datetime.now(),
        description="Payment for services rendered",
    )

    print(transaction)


if __name__ == "__main__":
    main()

from pirates import (
    Capitan,
    QuarterMaster,
    Officer,
    CannonOperator
)

class DataLoader:
    def load_pirates(self) -> list[Capitan | QuarterMaster | Officer | CannonOperator]:
        return  [
                Capitan("Harry"),
                QuarterMaster("Isabel"),
                Officer("Bootstrap Bill"),
                CannonOperator("Powder Joe"),
                Officer("Four Finger Fritz"),
                CannonOperator("Lady Joyce")
                ]
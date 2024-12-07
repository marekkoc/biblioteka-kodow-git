class Pouch:
    def __init__(self):
        self.items = ["Apple"]

    def add(self, item):  # Incorrect method name
        self.items.append(item)

    def getItem(self, index):
        return self.items[index]


# This function expects any container to have addItem and getItem methods
def useContainer(container):
    container.addItem("Orange")  # This will fail at runtime with AttributeError
    print(container.getItem(0))


def main() -> None:
    pouch = Pouch()
    useContainer(
        pouch
    )  # Raises AttributeError: 'Pouch' object has no attribute 'addItem'


if __name__ == "__main__":
    main()

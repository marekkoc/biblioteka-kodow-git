class Counter:
    def __init__(self, start: int = 0):
        self.value = start

    def __call__(self, increment: int = 1):
        self.value += increment
        return self.value


def main() -> None:
    counter = Counter(10)  # Start the counter at 10.
    print(counter.value)  # Print the initial value of the counter.
    print(counter())  # Increment by 1 (default) and print the new value.
    print(counter(5))  # Increment by 5 and print the new value.

    print((2).__class__)  # Output: <class 'int'>
    print(main.__class__)  # Output: <class 'function'>


if __name__ == "__main__":
    main()

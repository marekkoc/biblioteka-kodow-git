from collections import Counter

def count_fruits1(fruits: list[str]) -> dict[str, int]:
    # your code goes here
    dct: [str,int] = {}
    for fruit in fruits:
        if fruit in dct:
            dct[fruit] +=1
        else:
            dct[fruit] = 1
    return dct

def count_fruits2(fruits: list[str]) -> dict[str, int]:
    counter = Counter()
    for fruit in fruits:
        counter[fruit] +=1 if fruit in counter else 1
    return dict(counter)

def count_fruits3(fruits: list[str])-> dict[str, int]:
    return dict(Counter(fruits))





def main() -> None:
    assert count_fruits1(
        ["apple","banana","apple","cherry","banana","cherry","apple","apple","cherry","banana","cherry",]) == {"apple": 4, "banana": 3, "cherry": 4}

    assert count_fruits2(["apple","banana","apple","cherry","banana",]) == {"apple":2, "banana":2, "cherry":1}
    # add more tests

    assert count_fruits3(["apple","cherry","apple","cherry","banana", 'cherry']) == {"apple":2, "banana":1, "cherry":3}


    fruits: list[str] = [
        "apple",
        "banana",
        "apple",
        "cherry",
        "banana",
        "cherry",
        "apple",
        "apple",
        "cherry",
        "banana",
        "cherry",
    ]
    print(count_fruits3(fruits))

if __name__ == "__main__":
    main()

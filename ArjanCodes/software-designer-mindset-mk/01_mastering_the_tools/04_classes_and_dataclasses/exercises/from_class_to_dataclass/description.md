Convert the following classes into dataclasses such that the initializers that the dataclass generates have the same behavior as the regular class:

```python
class A:
    def __init__(self) -> None:
        self._length = 0

class B:
    def __init__(self, x: int, y: str = "hello", l: list[int] | None = None) -> None:
        self.x = x
        self.y = y
        self.l = [] if not l else l

class C:
    def __init__(self, a: int = 3) -> None:
        self.a = a
        self.b = a + 3
```

Compatible Python Versions: 3.10+
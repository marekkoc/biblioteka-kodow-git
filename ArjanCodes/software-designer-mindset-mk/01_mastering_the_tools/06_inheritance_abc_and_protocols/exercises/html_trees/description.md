Consider the following classes:

```python
@dataclass
class Div:
    parent: Div | None = None
    x: int = 0
    y: int = 0

    def compute_screen_position(self) -> tuple[int, int]:
        if not self.parent:
            return (self.x, self.y)
        parent_x, parent_y = self.parent.compute_screen_position()
        return (parent_x + self.x, parent_y + self.y)

@dataclass
class Button:
    parent: Div
    x: int
    y: int

    def click(self) -> None:
        print("Click!")

@dataclass
class Span:
    parent: Div
    x: int
    y: int
    text: str
```

Of course, HTML has many more different elements. In the elements above, there is some duplication (in particular, the parent, x and y instance variables). Also, we'd like to be able to compute the position of any type of element, not just divs and be able to combine different elements in a tree.

## a) Abstraction

Refactor the class hierarchy by introducing an abstract base class `HTMLElement` that divs, buttons, and spans are subclasses of. Minimize code duplication and make sure that each element is able to compute its position on the screen.

In order to get started more quickly, download the code for this exercise above (but don't look at the solution yet!).

Compatible Python Versions: 3.10+
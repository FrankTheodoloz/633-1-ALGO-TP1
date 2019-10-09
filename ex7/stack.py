class Stack:
    """
    Classe dont la responsabilité est de gérer un stack (LIFO)
    """

    def __init__(self) -> None:
        self.length = 5
        self.stack = [""] * self.length
        self.lastIn = -1

    def push(self, _value: str):
        if self.lastIn + 1 >= self.length: self.expand()
        self.stack[self.lastIn + 1] = _value
        self.lastIn += 1

    def pop(self) -> str:
        t = self.stack[self.lastIn]
        self.lastIn -= 1
        return t

    def is_empty(self) -> bool:
        return True if self.lastIn == -1 else False

    def expand(self):
        self.length *= 2
        new_stack = [""] * self.length
        i = 0
        while i < len(self.stack):
            new_stack[i] = self.stack[i]
            i += 1
        self.stack = new_stack

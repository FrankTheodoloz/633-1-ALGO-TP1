class Queue:
    """
    Classe dont la responsabilité est de gérer une queue (FIFO)
    """

    def __init__(self, _list: list = None) -> None:
        self.length = 5
        self.queue = [""] * self.length
        self.lastIn = -1
        self.lastOut = -1

        # can instantiate a queue with a list
        if _list: self.load(_list)

    def add(self, _value: str):
        if self.lastIn + 1 >= self.length: self.expand()
        self.queue[self.lastIn + 1] = _value
        self.lastIn += 1

    def remove(self) -> str:
        self.lastOut += 1
        t = self.queue[self.lastOut]
        return t

    def is_empty(self) -> bool:
        return True if self.lastOut == self.lastIn else False

    def expand(self):
        self.length *= 2
        new_queue = [""] * self.length
        i = 0
        while i < len(self.queue):
            new_queue[i] = self.queue[i]
            i += 1
        self.queue = new_queue

    def load(self, _list: list) -> None:
        for item in _list:
            self.add(item)

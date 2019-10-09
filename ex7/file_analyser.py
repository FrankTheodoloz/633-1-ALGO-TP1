import re
from ex7.charsstorage import CharsStorage
from ex7.stack import Stack


class FileAnalyser:
    """
    Fichier dont la responsabilité est de connaître l'algorithme qui permet de déterminer
    si le code est correct.
    """
    charsStorage = CharsStorage()

    def __init__(self, _content: str = 0) -> None:
        if len(_content) > 0:
            self.content = _content

    def analyse(self) -> bool:
        stack = Stack()

        # removes chars not in scope
        small_set = re.findall(r"[" + re.escape(self.charsStorage.regex) + "]", self.content)

        # for char in self.content:  # the looong way...
        for char in small_set:
            index = -1

            # when opening char is found
            if char in self.charsStorage.opening():

                # gets its index in CharsStorage
                index = self.charsStorage.opening().index(char)

                # pushes corresponding closing char in stack
                stack.push(self.charsStorage.closing()[index])

            # when closing char is found
            elif char in self.charsStorage.closing():

                # checks if it is the awaited char from the stack
                if char != stack.pop():
                    return False

        # if there is still something in the stack
        if not stack.is_empty(): return False

        return True

class CharsStorage:
    """
    Classe dont la responsabilité est de connaître les caractères ouvrants en fermants dans un fichier donné
    """

    def __init__(self) -> None:
        self.chars = [
            ["[", "{", "("],
            ["]", "}", ")"]  # same order as above
        ]

        # builds a string from the lists
        self.regex = ''.join(self.chars[0] + self.chars[1])

    def opening(self) -> list:
        return self.chars[0]

    def closing(self) -> list:
        return self.chars[1]

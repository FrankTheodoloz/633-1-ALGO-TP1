class ArrayList:
    """
    Classe dont la responsabilité est de gérer un tableau
    """

    def __init__(self):
        """
        Créer un tableau de caractères
        """
        self.list = 'Software Developer An organism that turns caffeine into software'.split(' ')

    def get(self, n: int):
        """
        Fonction qui permet de récupérer un élément du tableau
        :param n: indice de l'élément à retourner
        :return: un caractère à la position n
        """
        return self.list[n]


if __name__ == '__main__':
    liste = ArrayList()
    print(liste.get(3))

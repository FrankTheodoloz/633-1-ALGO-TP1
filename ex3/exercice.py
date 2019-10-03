import random


class NumberList:
    """
    Classe dont la responsabilité est gérer une liste de numéros
    """

    def __init__(self):
        """
        Constructeur qui génère 15 numéros au hasard entre 0 et 10
        """
        self.list = random.choices(range(0, 11), k=15)

    def get(self, n: int) -> int :
        """
        Retourne le numéro qui se trouve à l'indice n
        :param n: indice de la valeur
        :return: la valeur à l'indice n
        """
        return self.list[n]

    def max(self) -> int :
        """
        Trouve l'indice de la plus grande valeur dans le tableau
        Si plusieurs fois les mêmes valeurs, retourner le premier indice (plus à gauche)
        :return: indice de la plus grande valeur
        """
        max = -1
        index = -1
        #TODO: Votre code ici
        return index

if __name__ == '__main__':
    #Vos tests ici
    pass

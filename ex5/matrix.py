import random


class GenerateMatrix:
    def __generate_matrix(self, n: int = None, m : int = None) -> list:
        """
        Fonction permettant de générer une matrice de taille n x m
        Toutes les valeurs seront à False, sauf une valeur aléatoire à True
        :param n: taille de la largeur
        :param m: taille de la hauteur
        :return: matrice
        """
        if n is None:
            n = random.randint(1, 100)
        if m is None:
            m = random.randint(1, 100)

        matrix = [[False for column in range(m)] for row in range(n)]

        n = random.randint(0, n - 1)
        m = random.randint(0, m - 1)

        matrix[n][m] = True

        return matrix

    def random_matrix(self) -> list:
        return self.__generate_matrix()

    def matrix10(self) -> list:
        return self.__generate_matrix(10, 10)

    def matrix100(self) -> list:
        return self.__generate_matrix(100, 100)

    def matrix1000(self) -> list:
        return self.__generate_matrix(1000, 1000)

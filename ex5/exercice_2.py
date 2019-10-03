from ex5.matrix import GenerateMatrix


def find_point(matrix: list) -> list:
    """
    Fonction permettant de trouver un point caché dans une matrice.
    Implémentation d'un algorithme plus intelligent: Une fois le bon point trouvé, il faut le
    retouner immédiatement.
    La matrice contient toutes les valeurs à False, sauf le point à trouver (True).
    :param matrix: matrice contenant tous les points
    :return: Les coordonnées du point trouvé [x, y]
    """
    #TODO: Votre code ici
    return [-1, -1]

if __name__ == '__main__':
    # Ne pas modifier la ligne ci-dessous
    matrice = GenerateMatrix().random_matrix()

    # Vos tests ici
    point = find_point(matrice)

    print(point)

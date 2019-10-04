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
    point = [-1, -1]
    y = 0

    for value_y in matrix:  # parcours des lignes
        x = 0
        for value_x in value_y:  # parcours des colonnes
            if value_x:
                point = [x, y]
                return point
            x += 1
        y += 1


if __name__ == '__main__':
    # Ne pas modifier la ligne ci-dessous
    matrice = GenerateMatrix().random_matrix()

    # Vos tests ici
    print(find_point(matrice))

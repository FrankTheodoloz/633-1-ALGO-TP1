# def equation(a: int, b: int, c: int, n: int) -> list[dict['x', 'y', 'z']]:
# def equation(a: int, b: int, c: int, n: int) -> list[dict[str: int, str: int, str: int]]:
def equation(a: int, b: int, c: int, n: int) -> list:
    """
    Fonction qui permet de trouver les combinaisons de a, b et c qui résolvent l'equation
    Ces trois paramètres doivent être plus petits que n
    :param a: poids du x
    :param b: poids du y
    :param c: poids du z
    :param n: limite des valeurs de a, b, c
    :return: array de dictionnaires contenant chaque combinaison possible
    """
    # nb_essais = 0
    possibilites = []
    for x in range(n + 1):
        for y in range(n + 1):
            for z in range(n + 1):
                # nb_essais += 1
                if a * x + b * y + c * z == 100:  # 10 * 0 + 10 * 0 + 10 * 1 = 100 ?
                    possibilites.append({'x': x, 'y': y, 'z': z})
    # print(nb_essais)
    return possibilites


if __name__ == '__main__':
    print(equation(10, 10, 10, 10))  # 10*x + 10*y + 10*z
    # print(equation(5, 10, 20, 10))  # 5*x + 10*y + 20*z

def multiple_de(multiple: int, n: int):
    """
    Fonction permettant de savoir si un numéro est multiple d'un autre
    :param multiple: entier
    :param n: entier
    :return: true si n est multiple de "multiple", false si non
    """
    # if n % multiple == 0:
    #     return True
    # else:
    #     return False

    return True if n % multiple == 0 else False


if __name__ == '__main__':
    print(multiple_de(2, 10))  # True
    print(multiple_de(3, 20))  # False

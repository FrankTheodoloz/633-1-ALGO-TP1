def power_test(a: int, n: int, iter: int) -> int:
    """
    Calculer a^n en ayant une performance de log(n)
    n doit être un pouvoir de 2
    :param a: nombre entier
    :param n: exposant
    :param iter: nombre entier pour compter les itérations
    :return: résultat de a^n
    """
    if n == 1:
        print("itération =", iter)
        return a
    elif n % 2 != 0:
        print("l'exposant utilisé sera le pouvoir de 2 inférieur.")

    iter += 1
    return power_test(a * a, int(n / 2), iter)


def power(a: int, n: int) -> int:
    """
    Calculer a^n en ayant une performance de log(n)
    n doit être un pouvoir de 2
    :param a: nombre entier
    :param n: exposant
    :return: résultat de a^n
    """

    if n == 1: return a
    return power(a * a, int(n / 2))


if __name__ == '__main__':
    # print(power_test(3, 16, 0))
    print(power(3, 16))  # 16 = 4 itérations

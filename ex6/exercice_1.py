def power_iterative(a: int, n: int) -> int:
    """
    Calculer a^n
    :param a: nombre entier
    :param n: exposant
    :return: résultat de a^n
    """
    iter = 0
    result = a
    for i in range(1, n):
        iter += 1
        result = result * a
    print("itérations =", iter)
    return result


def power_recursive(a: int, n: int, iteration: int = 0) -> int:
    """
    Calculer a^n
    :param a: nombre entier
    :param n: exposant
    :param iteration: compteur
    :return: résultat de a^n
    """

    if n == 0:
        # print("itérations =", iteration)
        return 1
        # iteration += 1
    return a * power_recursive(a, n - 1, iteration)


if __name__ == '__main__':
    # print(power_iterative(3, 16))
    print(power_recursive(3, 16))

import matplotlib.pyplot as plt
import time
from ex4.exercice import equation


def test_equation(valeur_n: list, nb_executions: int):
    '''
    fonction qui va exécuter nb_executions fois equation avec valeur_n possibilités de chiffres
    la fonction s'exécutera pour évaluer chaque possibilité si elle est égale à 100
    :param valeur_n: int, pour les possibilités de 0 à n
    :param nb_executions: int, pour le nombre d'exécutions
    :return: float, la durée moyenne d'exécution
    '''

    x = []  # ordonnée: possibilités des chiffres n
    y = []  # abscisse: le temps

    for n in valeur_n:  # le nombre de possibilités
        x.append(n)

        start = time.time()
        for i in range(0, nb_executions):  # le nombre d'executions
            equation(10, 10, 10, n)
        temps = time.time() - start

        y.append(temps / float(nb_executions))  # le temps total divisé par le nombre d'exécution

    plt.plot(x, y, marker='o')
    plt.grid()
    plt.xlabel('Valeurs de n')
    plt.ylabel('Temps d\'éxécution moyen (secondes)')
    plt.title('Performance d\'exécution sur ' + str(nb_executions) + ' tests')
    plt.show()


if __name__ == '__main__':
    nb_executions = 1000
    # valeur_n = [10, 50, 100, 250, 500]  ## env. 30 sec. pour 1 exécution
    # valeur_n = [10, 100]  # moins d'une seconde pour 1 exécution
    # valeur_n = [1000]  # env 4 mn pour 1 exécution (1 milliards d'itérations)
    valeur_n = [10, 100, 1000]
    test_equation(valeur_n, nb_executions)

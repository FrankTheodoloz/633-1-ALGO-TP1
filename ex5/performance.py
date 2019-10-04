import matplotlib.pyplot as plt
import time
from ex5.matrix import GenerateMatrix
from ex5.exercice_1 import find_point as find_naive
from ex5.exercice_2 import find_point as find_amelioree


def compare(matrix: list) -> list:
    y_naive = -1
    start = time.time()
    find_naive(matrix)
    y_naive = time.time() - start

    y_amelioree = -1
    start = time.time()
    find_amelioree(matrix)
    y_amelioree = time.time() - start

    return [y_naive, y_amelioree]


def moy(list: list, nb_executions: int) -> float:
    sum = 0
    for i in list:
        sum += i
    return sum / (float(nb_executions))


x = []
y_naive_10 = []
y_naive_100 = []
y_naive_1000 = []
y_amelioree_10 = []
y_amelioree_100 = []
y_amelioree_1000 = []


def graf_perf_detail():  # Performance d'exécution DETAIL
    plt.plot(x, y_naive_10, color='green', label="naif 10x10")
    plt.plot(x, y_amelioree_10, color='green', linestyle='dashed', label="amélioré 10x10")

    plt.plot(x, y_naive_100, color='orange', label="naif 100x100")
    plt.plot(x, y_amelioree_100, color='orange', linestyle='dashed', label="amélioré 100x100")

    plt.plot(x, y_naive_1000, color='red', label="naif 1000x1000")
    plt.plot(x, y_amelioree_1000, color='red', linestyle='dashed', label="amélioré 1000x1000")

    plt.grid()
    plt.xlabel('matrice')
    plt.ylabel('Temps d\'éxécution (secondes)')
    plt.title('Performance d\'exécution sur ' + str(nb_executions) + ' matrices')
    plt.legend()
    plt.show()


def graf_perf_moyenne():  # Performance d'exécution MOYENNE
    plt.plot([10, 100, 1000],
             [moy(y_naive_10, nb_executions), moy(y_naive_100, nb_executions), moy(y_naive_1000, nb_executions)],
             color='blue', marker='o', linestyle='dashed', label="naive")

    plt.plot([10, 100, 1000],
             [moy(y_amelioree_10, nb_executions), moy(y_amelioree_100, nb_executions),
              moy(y_amelioree_1000, nb_executions)],
             color='red', marker='x', label="amélioré")

    plt.title('Performance moyenne d\'exécution sur ' + str(nb_executions) + ' matrices')
    plt.xlabel('taille matrice')
    plt.ylabel('Temps d\'éxécution (secondes)')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':

    nb_executions = 1000  # 1000 : env 1:10
    for i in range(1, nb_executions):
        x.append(i)
        result = compare(GenerateMatrix().matrix10())
        y_naive_10.append(result[0])
        y_amelioree_10.append(result[1])

        result = compare(GenerateMatrix().matrix100())
        y_naive_100.append(result[0])
        y_amelioree_100.append(result[1])

        result = compare(GenerateMatrix().matrix1000())
        y_naive_1000.append(result[0])
        y_amelioree_1000.append(result[1])

    # graf_perf_detail()
    graf_perf_moyenne()

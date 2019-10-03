import matplotlib.pyplot as plt
import time

'''
Ajouter une ligne dans votre graphique
Seuls les deux premiers paramètres sont obligatoires
Le premier paramètres correspond à toutes les valeurs x, et le deuxième correspond aux valeurs y
'''
plt.plot([1, 2, 3], [1, 2, 3], color='green', marker='o', linestyle='dashed', label="Linéaire")
plt.plot([1, 2, 3], [1, 4, 9], color='orange', marker='+', label='Carré')
plt.plot([1, 2, 3], [1, 8, 27], color='red', label='Cubique')
plt.xlabel('Abscisse')
plt.ylabel('Ordonnée')
plt.title('Exemple de graphique simple')
# Ajouter une grille à votre graphique
plt.grid()
# Afin que la légende s'affiche correctement, vous devez spécifier le paramètre label dans la fonction plot
plt.legend()
plt.show()
'''
Vous êtes libres de créer les graphiques comme vous le voulez, l'important c'est que l'on
puisse voir les éléments essentiels
'''

'''
Exemple d'utilisation pour une vraie fonction
'''

'''
Fonction qui a un temps d'exécution carré
C'est-à-dire, pour un x = 1, l'exécution prendra 1 seconde
Pour x = 2, l'exécution prendra 4 secondes
'''
def fun(x: int):
    # Attendre x^2 secondes avant de poursuivre l'exécution
    time.sleep(x ** 2)

x = []
y = []
for i in range(4):
    x.append(i)
    start = time.time()
    fun(i)
    temps = time.time() - start
    y.append(temps)
    print('Cela nous a pris {0} secondes pour éxécuter la valeur {1}!'.format(temps, i))


plt.plot(x, y)
plt.xlabel('Valeurs du i')
plt.ylabel('Temps d\'éxécution')
plt.title('Démonstration d\'un graphique')
plt.show()

from ex5.matrix import GenerateMatrix

# Matrice taille 10x10
matrice = GenerateMatrix().matrix10()
print(len(matrice))

# Matrice taille 100x100
matrice = GenerateMatrix().matrix100()
print(len(matrice))

# Matrice taille 1000x1000
matrice = GenerateMatrix().matrix1000()
print(len(matrice))

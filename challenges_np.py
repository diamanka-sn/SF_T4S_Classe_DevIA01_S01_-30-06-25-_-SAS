import numpy as np

#  Challenge 1

temperatures = np.array([18.5, 21.0, 19.2, 23.5, 17, 20.1, 22.3])
moyenne = np.mean(temperatures)
mediane = np.median(temperatures)
ecart_type = np.std(temperatures)

print(f"Temperatures: {temperatures}")
print(f"Moyenne : {moyenne:.2f} °C")
print(f"Médiane : {mediane:.2f} °C")
print(f"Écart-type : {ecart_type:.2f} °C\n")

# Challenge 2 
donnees = np.array([10, 20, 30, 40, 50])
moy = np.mean(donnees)
std = np.std(donnees)

donnees_normalisees = (donnees - moy) / std
print(f"{donnees_normalisees}")

# Challenge 3 
tableau1 = np.array([5, 10, 15, 20, 25])
tableau2 = np.array([5, 11, 15, 21, 24])

indices_diff = np.where(tableau1 != tableau2)[0]
print("Indices des differences :", indices_diff)

for idx in indices_diff:
    print(f"Index {idx} → t1: {tableau1[idx]}, t2: {tableau2[idx]}")

# Challenge 4 
matriceA = np.array([[2, 4], [1, 3]])
matriceB = np.array([[5, 2], [7, 6]])

produit = np.dot(matriceA, matriceB)
transposee = produit.T
inverse = np.linalg.inv(produit) if np.linalg.det(produit) != 0 else "Non inversible"

print("Matrice A :\n", matriceA)
print("Matrice B :\n", matriceB)
print("Produit A * B :\n", produit)
print("Transposee :\n", transposee)
print("Inverse :\n", inverse)
print()

# Challenge 5
valeurs = np.array([5, 12, 20, 7, 30, 2, 18])
seuil = 15
indices = np.where(valeurs > seuil)
valeurs_filtrees = valeurs[indices]

print(f"Valeurs : {valeurs}")
print(f"Valeurs > {seuil} : {valeurs_filtrees}")

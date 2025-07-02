# challenge 01
prenom = input("Quel est votre prenom ? ")
age = input("Quel est votre age ? ")
print(f"Bonjour {prenom}, vous avez {age} ans.")

# challenge 02
nom = input("Nom : ")
salaire_horaire = float(input("Salaire horaire  : "))
heures_travaillees = float(input("Nombre d'heures travaillees : "))

heures_supp = 0
if heures_travaillees > 40:
    heures_supp = heures_travaillees - 40
    heures_travaillees = 40

salaire_total = (heures_travaillees * salaire_horaire) + (heures_supp * salaire_horaire * 1.5)
print(f"{nom}, votre salaire total est de {salaire_total:.2f}.")

# challenge 03
try:
    salaire_horaire = float(input("Salaire horaire "))
    heures_travaillees = float(input("Nombre d'heures travaillees : "))
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")
    exit()

heures_supp = 0
if heures_travaillees > 40:
    heures_supp = heures_travaillees - 40
    heures_travaillees = 40

salaire_total = (heures_travaillees * salaire_horaire) + (heures_supp * salaire_horaire * 1.5)
print(f"{nom}, votre salaire total est de {salaire_total:.2f}")

# challenge 04
try:
    n1 = float(input("Entrez le premier nombre : "))
    n2 = float(input("Entrez le deuxième nombre : "))
except ValueError:
    print("Erreur : Entrez un nombre valide.")
    exit()

produit = n1 * n2
if produit > 0:
    print("Le produit est positif.")
elif produit < 0:
    print("Le produit est négatif.")
else:
    print("Le produit est nul.")

# challenge 05

try:
    N = int(input("Entrez un entier: "))
    if N < 1:
        print("Veuillez entrer un entier positif.")
        exit()
except ValueError:
    print("Erreur")
    exit()

somme = 0
i = 1
while i <= N:
    somme += i
    i += 1

print(f"La somme des entiers de 1 à {N} est {somme}.")

# challenge 06
chaine = input("Entrez une chaîne de caractères : ")
inversee = ""
i = len(chaine) - 1

while i >= 0:
    inversee += chaine[i]
    i -= 1

print(f"Chaîne originale: {chaine}")
print(f"Chaîne inversée: {inversee}")

# challenge 07
import math

try:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
except ValueError:
    print("Erreur : Entrez un nombre valide.")
    exit()

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distance entre les points est : {distance:.3f}")

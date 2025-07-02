import math

# Challenge 01
def horaire_sup(nom, salaire_horaire, heures_travaillees):
    heures_supp = 0
    if heures_travaillees > 40:
        heures_supp = heures_travaillees - 40
        heures_travaillees = 40
    salaire_total = (heures_travaillees * salaire_horaire) + (heures_supp * salaire_horaire * 1.5)
    return nom, salaire_total

# Challenge 02
def calculation(a, b):
    somme = a + b
    difference = a - b
    return somme, difference

# Challenge 03

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    return n * factorielle(n - 1)

def table_multiplication(m):
    table = []
    for i in range(1, 11):
        table.append(f"{m} x {i} = {m * i}")
    return table

def est_carre_parfait(L):
    if L < 0:
        return False
    racine = int(math.sqrt(L))
    return racine * racine == L

def afficher_caracteres(chaine):
    for c in chaine:
        print(c)

def mot_le_plus_long(phrase):
    mots = phrase.split()
    if not mots:
        return None
    mot_long = max(mots, key=len)
    return mot_long

def compter_occurrences(Ch):
    occurrences = {}
    for c in Ch:
        if c != " ":
            occurrences[c] = occurrences.get(c, 0) + 1
    return occurrences

if __name__ == "__main__":
    try:
        n = int(input("Entrez un entier pour calculer la factorielle : "))
    except ValueError:
        print("Entrée invalide.")
        exit()
    # fact = factorielle(n)

    print(f"{n}! = {factorielle(n)}")


    try:
        m = int(input("Entrez un entier pour afficher sa table de multiplication: "))
    except ValueError:
        print("Entrée invalide.")
        exit()
    print(f"Table de multiplication de {m}:")
    for ligne in table_multiplication(m):
        print(ligne)

    try:
        L = int(input("Entrez un entier pour vérifier s'il est un carre parfait : "))
    except ValueError:
        print("Entrée invalide.")
        exit()
    if est_carre_parfait(L):
        print(f"{L} est un carre parfait.")
    else:
        print(f"{L} n'est pas un carre parfait.")

    chaine = input("Entrez une chaîne de caracteres  ")
    print("Chaque caractère :")
    afficher_caracteres(chaine)

    phrase = input("Entrez une phrase : ")
    mot_long = mot_le_plus_long(phrase)
    if mot_long:
        print(f"Le mot le plus long est : {mot_long}")
    else:
        print("Aucun mot détecté.")

    Ch = input("Entrez une chaîne pour compter les occurrences de chaque caractere : ")
    occ = compter_occurrences(Ch)
    for caractere, nombre in sorted(occ.items()):
        print(f'Le caractère "{caractere}" figure {nombre} fois dans la chaine.')

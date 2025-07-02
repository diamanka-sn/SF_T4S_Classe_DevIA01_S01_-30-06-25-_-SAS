# Challenge 01
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

moyenne = sum(notes) / len(notes)
resultat = []
for note in notes:
    if note > moyenne:
        resultat.append(note)

print(resultat)


# Challenge 02
Ch1 = "Le langage Python est très populaire"
Ch2 = "Python est un langage puissant"

mots1 = Ch1.lower().split()
mots2 = Ch2.lower().split()
communs = []
for mot in mots1:
    if mot in mots2 and mot not in communs:
        communs.append(mot)

print(communs)

# challenge 03
stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]

chaines = []
nombres = []

for item in stock:
    if type(item) == str:
        chaines.append(item)
    else:
        nombres.append(item)

for i in range(len(chaines)):
    for j in range(0, len(chaines)-i-1):
        if chaines[j].lower() > chaines[j+1].lower():
            chaines[j], chaines[j+1] = chaines[j+1], chaines[j]
            
for i in range(len(nombres)):
    for j in range(0, len(nombres)-i-1):
        if nombres[j] < nombres[j+1]:
            nombres[j], nombres[j+1] = nombres[j+1], nombres[j]

print("Chaînes triées :", chaines)
print("Nombres triés :", nombres)


# Challenge 04
def rechercheElement(element, liste):
    for i in range(len(liste)):
        if liste[i] == element:
            return i
    return False

print(rechercheElement(3, [1,2,3,4]))
print(rechercheElement(5, [1,2,3,4]))

# Challenge 05
L = [7 , 23 , 5 , 23 , 7 , 19 , 23 , 12 , 29]
a = 23

compteur = 0
for element in L:
    if element == a:
        compteur = compteur + 1

print(compteur)

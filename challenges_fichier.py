import os
import shutil

# challenge 01
repertoire = "fichiers_txt"
contenu_total = ""

if os.path.exists(repertoire):
    for nom_fichier in os.listdir(repertoire):
        if nom_fichier.endswith(".txt"):
            chemin_fichier = os.path.join(repertoire, nom_fichier)
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                contenu_total += f.read() + "\n"
    print("Contenu combine de tous les fichiers texte :\n")
    print(contenu_total)
else:
    print(f"Le répertoire '{repertoire}' n'existe pas.")

# challenge 02  
config_path = os.path.join("config", "config.yaml")

if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as config_file:
        contenu_config = config_file.read()
    print("Contenu de config.yaml :\n")
    print(contenu_config)
else:
    print("Le fichier config.yaml est introuvable.")

# challenge 03
source_dir = "donnees_source"
destination_dir = "donnees_csv"

if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)

for fichier in os.listdir(source_dir):
    if fichier.endswith(".csv"):
        source_fichier = os.path.join(source_dir, fichier)
        destination_fichier = os.path.join(destination_dir, fichier)
        shutil.copy(source_fichier, destination_fichier)
        print(f"Copié : {fichier}")

# challenge 04
repertoire_principal = "IA"
sous_dossiers = ["data", "scripts", "outputs", "docs"]

if not os.path.exists(repertoire_principal):
    os.mkdir(repertoire_principal)
    print(f"Repertoire principal cree : {repertoire_principal}")

for dossier in sous_dossiers:
    chemin = os.path.join(repertoire_principal, dossier)
    if not os.path.exists(chemin):
        os.mkdir(chemin)
        print(f"Sous-repertoire cree : {chemin}")

# challenge 05
nom_fichier = "exemple.txt"
lignes = ["Bonjour", "le monde", "."]

with open(nom_fichier, "w", encoding="utf-8") as f:
    for ligne in lignes:
        f.write(ligne + "\n")

print(f"Le fichier '{nom_fichier}' a ete écrit avec succes.")

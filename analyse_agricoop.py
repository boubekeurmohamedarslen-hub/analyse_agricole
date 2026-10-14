import csv

# 1. Créer une liste vide
adherents = []

# 2. Ouvrir le fichier
with open("agricoop_adherents (1).csv", encoding="utf-8-sig") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=";")

    # 3. Ajouter chaque ligne dans la liste
    for ligne in lecteur:
        adherents.append(ligne)

# 4. Afficher le premier adhérent
print(adherents[0])
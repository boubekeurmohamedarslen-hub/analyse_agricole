import pandas as pd

# Charger le fichier des adhérents (toutes les colonnes en texte pour garder les zéros des SIRET et codes postaux)
adherents = pd.read_csv("data/agricoop_adherents.csv", sep=";", dtype=str, encoding="utf-8-sig", keep_default_na=False)


# Créer le tableau
df = adherents

# Compter les lignes avant
nombre_avant = len(df)

# Garder une seule ligne par SIRET
df = df.drop_duplicates(subset="siret")

# Compter les lignes après
nombre_apres = len(df)

# Calculer le nombre de doublons supprimés
nombre_doublons = nombre_avant - nombre_apres

# Afficher le tableau
print(df.to_string(index=False))

# Afficher les résultats
print("Avant :", nombre_avant)
print("Doublons supprimés :", nombre_doublons)
print("Après :", nombre_apres)

# Colonnes critiques
critiques = ["id_adherent", "nom_exploitation", "siret", "iban", "statut"]

# Colonnes sensibles dans le contexte du fichier
sensibles = ["nom_exploitation", "siret", "iban", "email", "telephone", "commune", "code_postal"]

# Colonnes contrôlées par des référentiels
references = ["statut", "commune", "code_postal"]

print(df[critiques].to_string(index=False))

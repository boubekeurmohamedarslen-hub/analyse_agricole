# Agricoop : qualité des données adhérents

Exercice EPSI Paris (Expert IA & Data Science), octobre 2026. Le fichier des adhérents d'une coopérative agricole fictive, Agricoop, doit servir de référentiel. Avant de l'utiliser, il faut savoir s'il est fiable : doublons, champs vides, formats faux, valeurs incohérentes.

## Données

`data/agricoop_adherents.csv` : 800 lignes, 11 colonnes, séparateur `;`.

| Colonne | Exemple |
|---|---|
| `id_adherent` | A0001 |
| `nom_exploitation` | nom de l'exploitant |
| `siret` | 14 chiffres |
| `iban` | FR76… |
| `email`, `telephone` | coordonnées |
| `commune`, `code_postal` | Pas-de-Calais (62) et Somme (80) |
| `date_adhesion`, `date_maj` | JJ/MM/AAAA |
| `statut` | ACTIF, SORTI, Retraité… |

Le fichier contient des données personnelles (IBAN, e-mails, téléphones). Il s'agit du jeu de données fourni pour l'exercice.

## Scripts

| Fichier | Rôle |
|---|---|
| `analyse_agricoop.py` | lecture du CSV avec le module `csv` et affichage du premier adhérent |
| `nettoyage_doublons_siret.py` | chargement avec Pandas, suppression des doublons de SIRET, définition des colonnes critiques, sensibles et contrôlées par référentiel |

```bash
pip install pandas
python nettoyage_doublons_siret.py
```

## Résultat

| | Lignes |
|---|---|
| Avant nettoyage | 800 |
| Doublons de SIRET supprimés | 40 |
| Après nettoyage | 760 |

Le script classe aussi les colonnes en trois groupes :

- critiques, sans lesquelles la ligne est inutilisable : `id_adherent`, `nom_exploitation`, `siret`, `iban`, `statut`
- sensibles au sens du RGPD : `nom_exploitation`, `siret`, `iban`, `email`, `telephone`, `commune`, `code_postal`
- à contrôler contre un référentiel : `statut`, `commune`, `code_postal`

## Anomalies encore présentes dans le fichier

- `statut` écrit de sept façons (ACTIF, Actif, actif, SORTI, sorti, Inactif, Retraité) : à normaliser
- 56 IBAN et 31 e-mails vides
- 16 e-mails mal formés et 14 IBAN dont la clé de contrôle (modulo 97) est fausse

## Compétences

Python • Pandas • qualité des données • RGPD

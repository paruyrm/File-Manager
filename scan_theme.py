import os

# Chemin vers le dossier theme
theme_folder = "./theme"  # Utilisation de "./theme" pour indiquer le dossier 'theme' dans le même répertoire que le script

# Liste pour stocker tous les fichiers .qss trouvés
all_style_sheets = []

# Parcourir récursivement tous les sous-dossiers du dossier theme
for root, dirs, files in os.walk(theme_folder):
    for file in files:
        if file.endswith(".qss"):
            # Construire le chemin absolu du fichier .qss trouvé
            file_path = os.path.join(root, file)
            all_style_sheets.append(file_path)

# Trier la liste de fichiers .qss trouvés
all_style_sheets.sort()

# Afficher les fichiers .qss trouvés
print("Fichiers .qss trouvés :")
for file_path in all_style_sheets:
    print(file_path)

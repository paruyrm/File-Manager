import os

# Liste des fichiers .qss trouvés
styleSheets = [os.path.join(root, file) 
               for root, _, files in os.walk("./theme") 
               for file in files if file.endswith(".qss")]

# Tri des fichiers sans tenir compte de la casse
styleSheets.sort(key=lambda file: file.lower())

# Affichage des fichiers trouvés
print(styleSheets)
# for file_path in styleSheets:
#     print(file_path)

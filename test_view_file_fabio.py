from toolbox import os

print('')

for filename in os.listdir("C:\\Users\\Formation\\Documents\\GitHub\\LIC"):
   print(filename)
   

print('-------------')
# shutil.copy2("mon_fichier_a_copier","son_nouvel_emplacement")          →     Copier un fichier    
# shutil.move("mon_fichier_ou_dossier_a_deplacer","son_nouvel_emplacement")          →     Deplacer  un fichier    
# os.remove(path)          →   Supprime le fichier / dossier indiqué
# os.rename(old, new)      →   Renomme le fichier / dossier indiqué
# os.makedirs('chemin/du/nouveau/dossier') → Créer un dossier 
# os.rename('ancien_nom', 'nouveau_nom') → Renommer un fichier ou un dossier :
# nom_fichier, extension = os.path.splitext('chemin/du/fichier.txt')          →          Obtenir l'extension d'un fichier

for element in os.listdir('C:\\Users\\Formation\\Documents\\GitHub\\LIC'):
    chemin_complet = os.path.join('C:\\Users\\Formation\\Documents\\GitHub\\LIC', element)
    if os.path.isfile(chemin_complet):
        print(f"Fichier: {element}")
    elif os.path.isdir(chemin_complet):
        print(f"Dossier: {element}")


# Peut servir pour la recherche 
# Vérifie si un fichier existe
# if os.path.exists("mon_fichier.txt"):
#     print("Le fichier existe.")
# else:
#     print("Le fichier n'existe pas.")
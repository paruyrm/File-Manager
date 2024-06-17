from toolbox import os
from toolbox import mb
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName=input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path) 
    mb.showinfo('confirmation', "File Renamed !")
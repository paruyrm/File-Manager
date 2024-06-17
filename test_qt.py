	

import sys

from PySide6.QtCore import QDir, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTreeView, QVBoxLayout, QFileSystemModel


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # On change le titre de la fenêtre.
        self.setWindowTitle("PyFile Manager")
        
        # On change l'icône affichée dans le bandeau supérieur de la fenêtre.
        # self.setWindowIcon(QIcon("icons/file.png"))
        
        # On retaille la fenêtre (800 pixels de large et 600 en hauteur).
        self.resize(800, 600)

        # Le type QWidget représente un conteneur de widgets (et il est lui-même un widget).
        # On crée une instance que l'on va mettre au centre de la fenêtre.
        centralArea = QWidget()
        
        # On lui met une couleur d'arrière-plan, histoire de bien le voir.
        # centralArea.setStyleSheet("background: #419eee")
        
        # On injecte ce widget en tant que zone centrale.
        self.setCentralWidget(centralArea)
        
        button = QPushButton("This is a button", centralArea)
        button.setGeometry(320, 50, 270, 30)
        button.clicked.connect(self.buttonClicked)

        
        treeModel = QFileSystemModel()
        treeModel.setRootPath(QDir.currentPath())

        treeView = QTreeView()
        treeView.setModel(treeModel)

        layout = QVBoxLayout(self)
        layout.addWidget(treeView)
        self.setLayout(layout)
        
        
        
    @Slot()      # Pensez à importer le décorateur : from PySide6.QtCore import Slot
    def buttonClicked(self):
        btn = self.sender()
        print(f"Button <{btn.text()}> clicked")
    



if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # On instancie une fenêtre graphique et l'affiche.
    myWindow = MyWindow()
    myWindow.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())















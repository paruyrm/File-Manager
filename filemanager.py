# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QFileIconProvider
from ui_filemanager import Ui_FileManager
from PySide6.QtCore import QModelIndex

class FileManager(QMainWindow, Ui_FileManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        self.model = QFileSystemModel()
        self.model.setRootPath('/')  # Set the root path

        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(''))  # Set the root index to show the entire filesystem

        # Optionally, hide columns you don't want to display
        self.treeView.setColumnHidden(1, True)  # Hide size
        self.treeView.setColumnHidden(2, True)  # Hide file type
        self.treeView.setColumnHidden(3, True)  # Hide date modified
        
        self.model.setIconProvider(QFileIconProvider())

    def initUI(self):
        # You can connect signals to slots here, if needed
        self.actionNouveau.triggered.connect(self.new_file)
        self.actionCopier.triggered.connect(self.copy_file)
        self.actionCouper.triggered.connect(self.cut_file)
        self.actionColler.triggered.connect(self.paste_file)
        self.actionSauvegarder.triggered.connect(self.save_file)
        self.treeView.clicked.connect(self.treeview_select)

    def treeview_select(self, index : QModelIndex) :
        file_path = self.model.filePath(index)
        file_info = self.model.fileInfo(index)

        # Get details
        file_name = file_info.fileName()
        file_size = file_info.size()
        file_type = file_info.isDir() and "Directory" or "File"
        file_date_modified = file_info.lastModified().toString("dd/MM/yyyy hh:mm")

        self.lbl_chemin.setText("Chemin : " + file_path)
        print(f"Path: {file_path}")
        print(f"Name: {file_name}")
        print(f"Size: {file_size} bytes")
        print(f"Type: {file_type}")
        print(f"Date Modified: {file_date_modified}")
        
        
    def new_file(self):
        # Implement the functionality for creating a new file
        print("New File action triggered")

    def copy_file(self):
        # Implement the functionality for copying a file
        print("Copy action triggered")

    def cut_file(self):
        # Implement the functionality for cutting a file
        print("Cut action triggered")

    def paste_file(self):
        # Implement the functionality for pasting a file
        print("Paste action triggered")

    def save_file(self):
        # Implement the functionality for saving a file
        print("Save action triggered")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec())

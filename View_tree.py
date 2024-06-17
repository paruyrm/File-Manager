	

import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QWidget, QTreeView, QVBoxLayout, QFileSystemModel, QApplication


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        treeModel = QFileSystemModel()
        treeModel.setRootPath(QDir.currentPath())

        treeView = QTreeView()
        treeView.setModel(treeModel)

        layout = QVBoxLayout(self)
        layout.addWidget(treeView)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())

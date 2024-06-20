# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileManagerBIEZBH.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSplitter, QStatusBar, QToolBar, QTreeView,
    QVBoxLayout, QWidget)

class Ui_FileManager(object):
    def setupUi(self, FileManager):
        if not FileManager.objectName():
            FileManager.setObjectName(u"FileManager")
        FileManager.resize(1012, 609)
        FileManager.setUnifiedTitleAndToolBarOnMac(False)
        self.actionNouveau = QAction(FileManager)
        self.actionNouveau.setObjectName(u"actionNouveau")
        self.actionCopier = QAction(FileManager)
        self.actionCopier.setObjectName(u"actionCopier")
        self.actionCouper = QAction(FileManager)
        self.actionCouper.setObjectName(u"actionCouper")
        self.actionColler = QAction(FileManager)
        self.actionColler.setObjectName(u"actionColler")
        self.actionSauvegarder = QAction(FileManager)
        self.actionSauvegarder.setObjectName(u"actionSauvegarder")
        self.centralwidget = QWidget(FileManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.panel_treeview = QWidget(self.splitter)
        self.panel_treeview.setObjectName(u"panel_treeview")
        self.panel_treeview.setStyleSheet(u"background-color: rgb(140, 140, 140);")
        self.verticalLayout_2 = QVBoxLayout(self.panel_treeview)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeView = QTreeView(self.panel_treeview)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.verticalLayout_2.addWidget(self.treeView)

        self.splitter.addWidget(self.panel_treeview)
        self.panel_listview = QWidget(self.splitter)
        self.panel_listview.setObjectName(u"panel_listview")
        self.panel_listview.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.verticalLayout_3 = QVBoxLayout(self.panel_listview)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listView = QListView(self.panel_listview)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.verticalLayout_3.addWidget(self.listView)

        self.splitter.addWidget(self.panel_listview)
        self.panel_preview = QWidget(self.splitter)
        self.panel_preview.setObjectName(u"panel_preview")
        self.panel_preview.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.panel_preview)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_preview = QLabel(self.panel_preview)
        self.lbl_preview.setObjectName(u"lbl_preview")

        self.verticalLayout_4.addWidget(self.lbl_preview)

        self.widget = QWidget(self.panel_preview)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_nom = QLabel(self.widget)
        self.lbl_nom.setObjectName(u"lbl_nom")
        self.lbl_nom.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.lbl_nom)

        self.lbl_chemin = QLabel(self.widget)
        self.lbl_chemin.setObjectName(u"lbl_chemin")
        self.lbl_chemin.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.lbl_chemin)

        self.lbl_taille = QLabel(self.widget)
        self.lbl_taille.setObjectName(u"lbl_taille")
        self.lbl_taille.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.lbl_taille)

        self.lbl_date = QLabel(self.widget)
        self.lbl_date.setObjectName(u"lbl_date")
        self.lbl_date.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.lbl_date)

        self.lbl_type = QLabel(self.widget)
        self.lbl_type.setObjectName(u"lbl_type")
        self.lbl_type.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.lbl_type)


        self.verticalLayout_4.addWidget(self.widget)

        self.splitter.addWidget(self.panel_preview)

        self.verticalLayout.addWidget(self.splitter)

        FileManager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FileManager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1012, 33))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        FileManager.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FileManager)
        self.statusbar.setObjectName(u"statusbar")
        FileManager.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(FileManager)
        self.toolBar.setObjectName(u"toolBar")
        FileManager.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionCopier)
        self.menuFichier.addAction(self.actionCouper)
        self.menuFichier.addAction(self.actionColler)
        self.menuFichier.addAction(self.actionSauvegarder)

        self.retranslateUi(FileManager)

        QMetaObject.connectSlotsByName(FileManager)
    # setupUi

    def retranslateUi(self, FileManager):
        FileManager.setWindowTitle(QCoreApplication.translate("FileManager", u"MainWindow", None))
        self.actionNouveau.setText(QCoreApplication.translate("FileManager", u"Nouveau", None))
        self.actionCopier.setText(QCoreApplication.translate("FileManager", u"Copier", None))
        self.actionCouper.setText(QCoreApplication.translate("FileManager", u"Couper", None))
        self.actionColler.setText(QCoreApplication.translate("FileManager", u"Coller", None))
        self.actionSauvegarder.setText(QCoreApplication.translate("FileManager", u"Sauvegarder", None))
        self.lbl_preview.setText(QCoreApplication.translate("FileManager", u"TextLabel", None))
        self.lbl_nom.setText(QCoreApplication.translate("FileManager", u"Nom", None))
        self.lbl_chemin.setText(QCoreApplication.translate("FileManager", u"Chemin", None))
        self.lbl_taille.setText(QCoreApplication.translate("FileManager", u"Taille", None))
        self.lbl_date.setText(QCoreApplication.translate("FileManager", u"Date de modification", None))
        self.lbl_type.setText(QCoreApplication.translate("FileManager", u"Type", None))
        self.menuFichier.setTitle(QCoreApplication.translate("FileManager", u"Fichier", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("FileManager", u"toolBar", None))
    # retranslateUi


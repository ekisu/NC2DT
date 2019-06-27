# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.beatmapSearchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.beatmapSearchLineEdit.setObjectName("beatmapSearchLineEdit")
        self.horizontalLayout.addWidget(self.beatmapSearchLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.beatmapsListView = QtWidgets.QListView(self.centralwidget)
        self.beatmapsListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.beatmapsListView.setObjectName("beatmapsListView")
        self.verticalLayout.addWidget(self.beatmapsListView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChangeOsuPath = QtWidgets.QAction(MainWindow)
        self.actionChangeOsuPath.setObjectName("actionChangeOsuPath")
        self.menuSettings.addAction(self.actionChangeOsuPath)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NC2DT"))
        self.label.setText(_translate("MainWindow", "Beatmap search:"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionChangeOsuPath.setText(_translate("MainWindow", "Change osu! path"))


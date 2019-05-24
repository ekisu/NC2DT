# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/beatmap_details.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BeatmapDetails(object):
    def setupUi(self, BeatmapDetails):
        BeatmapDetails.setObjectName("BeatmapDetails")
        BeatmapDetails.resize(400, 174)
        self.verticalLayout = QtWidgets.QVBoxLayout(BeatmapDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(BeatmapDetails)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.artistLabel = QtWidgets.QLabel(BeatmapDetails)
        self.artistLabel.setObjectName("artistLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.artistLabel)
        self.label_3 = QtWidgets.QLabel(BeatmapDetails)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.titleLabel = QtWidgets.QLabel(BeatmapDetails)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.titleLabel)
        self.label_5 = QtWidgets.QLabel(BeatmapDetails)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.creatorLabel = QtWidgets.QLabel(BeatmapDetails)
        self.creatorLabel.setObjectName("creatorLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.creatorLabel)
        self.label_7 = QtWidgets.QLabel(BeatmapDetails)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.difficultyLabel = QtWidgets.QLabel(BeatmapDetails)
        self.difficultyLabel.setObjectName("difficultyLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.difficultyLabel)
        self.label_9 = QtWidgets.QLabel(BeatmapDetails)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.audioLabel = QtWidgets.QLabel(BeatmapDetails)
        self.audioLabel.setObjectName("audioLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.audioLabel)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.createConvertedAudioButton = QtWidgets.QPushButton(BeatmapDetails)
        self.createConvertedAudioButton.setEnabled(True)
        self.createConvertedAudioButton.setObjectName("createConvertedAudioButton")
        self.horizontalLayout.addWidget(self.createConvertedAudioButton)
        self.switchAudioButton = QtWidgets.QPushButton(BeatmapDetails)
        self.switchAudioButton.setObjectName("switchAudioButton")
        self.horizontalLayout.addWidget(self.switchAudioButton)
        self.closeButton = QtWidgets.QPushButton(BeatmapDetails)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(BeatmapDetails)
        self.closeButton.clicked.connect(BeatmapDetails.close)
        QtCore.QMetaObject.connectSlotsByName(BeatmapDetails)

    def retranslateUi(self, BeatmapDetails):
        _translate = QtCore.QCoreApplication.translate
        BeatmapDetails.setWindowTitle(_translate("BeatmapDetails", "Beatmap Details"))
        self.label.setText(_translate("BeatmapDetails", "Artist:"))
        self.artistLabel.setText(_translate("BeatmapDetails", "TextLabel"))
        self.label_3.setText(_translate("BeatmapDetails", "Title:"))
        self.titleLabel.setText(_translate("BeatmapDetails", "TextLabel"))
        self.label_5.setText(_translate("BeatmapDetails", "Creator:"))
        self.creatorLabel.setText(_translate("BeatmapDetails", "TextLabel"))
        self.label_7.setText(_translate("BeatmapDetails", "Difficulty:"))
        self.difficultyLabel.setText(_translate("BeatmapDetails", "TextLabel"))
        self.label_9.setText(_translate("BeatmapDetails", "Audio File:"))
        self.audioLabel.setText(_translate("BeatmapDetails", "TextLabel"))
        self.createConvertedAudioButton.setText(_translate("BeatmapDetails", "Create Converted Audio"))
        self.switchAudioButton.setText(_translate("BeatmapDetails", "Switch to NC2DT Audio"))
        self.closeButton.setText(_translate("BeatmapDetails", "Close"))


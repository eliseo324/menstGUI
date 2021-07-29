# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafica.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_grafica(object):
    def setupUi(self, MainWindow_grafica):
        MainWindow_grafica.setObjectName("MainWindow_grafica")
        MainWindow_grafica.resize(788, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow_grafica)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_descripcion = QtWidgets.QPushButton(self.centralwidget)
        self.Button_descripcion.setObjectName("Button_descripcion")
        self.horizontalLayout.addWidget(self.Button_descripcion)
        spacerItem = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow_grafica.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_grafica)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_grafica)

    def retranslateUi(self, MainWindow_grafica):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_grafica.setWindowTitle(_translate("MainWindow_grafica", "Gráfica"))
        self.Button_descripcion.setText(_translate("MainWindow_grafica", "Ir a la descripción del día"))

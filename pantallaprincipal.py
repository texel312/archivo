# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantallaprincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 800)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.stackedWidget.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/Pantalla Grande.png);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.principal = QtWidgets.QWidget()
        self.principal.setObjectName("principal")
        self.label = QtWidgets.QLabel(self.principal)
        self.label.setGeometry(QtCore.QRect(50, 550, 62, 62))
        self.label.setStyleSheet("border-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/apagado.gif);\n"
"border-radius: 15px;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(0)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.principal)
        self.label2.setGeometry(QtCore.QRect(205, 550, 62, 62))
        self.label2.setStyleSheet("border-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/apagado.gif);\n"
"border-radius: 15px;")
        self.label2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label2.setMidLineWidth(0)
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.principal)
        self.label3.setGeometry(QtCore.QRect(360, 550, 62, 62))
        self.label3.setStyleSheet("border-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/apagado.gif);\n"
"border-radius: 15px;")
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.principal)
        self.label4.setGeometry(QtCore.QRect(515, 550, 62, 62))
        self.label4.setStyleSheet("border-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/apagado.gif);\n"
"border-radius: 15px;")
        self.label4.setText("")
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.principal)
        self.label5.setGeometry(QtCore.QRect(930, 300, 400, 450))
        self.label5.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/figura_mujer.png);\n"
"")
        self.label5.setText("")
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(self.principal)
        self.label6.setGeometry(QtCore.QRect(675, 540, 50, 130))
        self.label6.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal1_desac.png);\n"
"")
        self.label6.setText("")
        self.label6.setObjectName("label6")
        self.label7 = QtWidgets.QLabel(self.principal)
        self.label7.setGeometry(QtCore.QRect(760, 540, 40, 130))
        self.label7.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal2_desac.png);")
        self.label7.setText("")
        self.label7.setObjectName("label7")
        self.label8 = QtWidgets.QLabel(self.principal)
        self.label8.setGeometry(QtCore.QRect(835, 540, 30, 130))
        self.label8.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal3_desac.png);")
        self.label8.setText("")
        self.label8.setObjectName("label8")
        self.label9 = QtWidgets.QLabel(self.principal)
        self.label9.setGeometry(QtCore.QRect(905, 540, 30, 130))
        self.label9.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal4_desac.png);")
        self.label9.setText("")
        self.label9.setObjectName("label9")
        self.label2.raise_()
        self.label3.raise_()
        self.label4.raise_()
        self.label.raise_()
        self.label5.raise_()
        self.label6.raise_()
        self.label9.raise_()
        self.label7.raise_()
        self.label8.raise_()
        self.stackedWidget.addWidget(self.principal)
        self.inicio = QtWidgets.QWidget()
        self.inicio.setObjectName("inicio")
        self.stackedWidget.addWidget(self.inicio)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


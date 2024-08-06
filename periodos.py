# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'periodos.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Periodos(object):
    def setupUi(self, Periodos):
        Periodos.setObjectName("Periodos")
        Periodos.setWindowModality(QtCore.Qt.ApplicationModal)
        Periodos.resize(521, 275)
        Periodos.setMinimumSize(QtCore.QSize(0, 0))
        Periodos.setMaximumSize(QtCore.QSize(16000000, 16000000))
        self.centralwidget = QtWidgets.QWidget(Periodos)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16000000, 16000000))
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Crear_periodo = QtWidgets.QPushButton(self.frame)
        self.Crear_periodo.setAcceptDrops(False)
        self.Crear_periodo.setObjectName("Crear_periodo")
        self.horizontalLayout.addWidget(self.Crear_periodo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cerrar = QtWidgets.QPushButton(self.frame)
        self.cerrar.setObjectName("cerrar")
        self.horizontalLayout.addWidget(self.cerrar)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame)
        Periodos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Periodos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 22))
        self.menubar.setObjectName("menubar")
        Periodos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Periodos)
        self.statusbar.setObjectName("statusbar")
        Periodos.setStatusBar(self.statusbar)

        self.retranslateUi(Periodos)
        QtCore.QMetaObject.connectSlotsByName(Periodos)
        Periodos.setTabOrder(self.Crear_periodo, self.tableWidget)

    def retranslateUi(self, Periodos):
        _translate = QtCore.QCoreApplication.translate
        Periodos.setWindowTitle(_translate("Periodos", "Periodos"))
        self.label.setText(_translate("Periodos", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Listado de periodos</span></p></body></html>"))
        self.tableWidget.setWhatsThis(_translate("Periodos", "tabla"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Periodos", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Periodos", "Fecha de Inicio"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Periodos", "Fecha fin"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Periodos", "Estatus"))
        self.Crear_periodo.setToolTip(_translate("Periodos", "<html><head/><body><p>Presione este botón para crear un nuevo período.</p></body></html>"))
        self.Crear_periodo.setText(_translate("Periodos", "Crear Período"))
        self.cerrar.setText(_translate("Periodos", "Cerrar"))

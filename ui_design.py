# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 781, 561))
        self.gestMuebles = QWidget()
        self.gestMuebles.setObjectName(u"gestMuebles")
        self.formLayoutWidget = QWidget(self.gestMuebles)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 291, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.addMueble = QPushButton(self.formLayoutWidget)
        self.addMueble.setObjectName(u"addMueble")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.addMueble)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)

        self.delMueble = QPushButton(self.formLayoutWidget)
        self.delMueble.setObjectName(u"delMueble")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.delMueble)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.modMueble = QPushButton(self.formLayoutWidget)
        self.modMueble.setObjectName(u"modMueble")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.modMueble)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)

        self.listMuebles = QPushButton(self.formLayoutWidget)
        self.listMuebles.setObjectName(u"listMuebles")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.listMuebles)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)

        self.verticalLayoutWidget = QWidget(self.gestMuebles)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(480, 10, 231, 371))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.idMueble = QLineEdit(self.verticalLayoutWidget)
        self.idMueble.setObjectName(u"idMueble")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.idMueble)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.nombreMueble = QLineEdit(self.verticalLayoutWidget)
        self.nombreMueble.setObjectName(u"nombreMueble")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.nombreMueble)

        self.precioMueble = QLineEdit(self.verticalLayoutWidget)
        self.precioMueble.setObjectName(u"precioMueble")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.precioMueble)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.alturaMueble = QLineEdit(self.verticalLayoutWidget)
        self.alturaMueble.setObjectName(u"alturaMueble")

        self.verticalLayout_2.addWidget(self.alturaMueble)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.anchoMueble = QLineEdit(self.verticalLayoutWidget)
        self.anchoMueble.setObjectName(u"anchoMueble")

        self.verticalLayout_2.addWidget(self.anchoMueble)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.largoMueble = QLineEdit(self.verticalLayoutWidget)
        self.largoMueble.setObjectName(u"largoMueble")

        self.verticalLayout_2.addWidget(self.largoMueble)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.verticalLayout_2)

        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.dimensionesFinales = QLineEdit(self.verticalLayoutWidget)
        self.dimensionesFinales.setObjectName(u"dimensionesFinales")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.dimensionesFinales)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.productos = QTableWidget(self.gestMuebles)
        self.productos.setObjectName(u"productos")
        self.productos.setGeometry(QRect(0, 140, 461, 389))
        self.tabWidget.addTab(self.gestMuebles, "")
        self.genPedidos = QWidget()
        self.genPedidos.setObjectName(u"genPedidos")
        self.formLayoutWidget_2 = QWidget(self.genPedidos)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(20, 20, 241, 91))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.idPedido = QLineEdit(self.formLayoutWidget_2)
        self.idPedido.setObjectName(u"idPedido")
        self.idPedido.setEnabled(False)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.idPedido)

        self.label_15 = QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.idMueblePedir = QLineEdit(self.formLayoutWidget_2)
        self.idMueblePedir.setObjectName(u"idMueblePedir")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.idMueblePedir)

        self.cantidad = QLineEdit(self.formLayoutWidget_2)
        self.cantidad.setObjectName(u"cantidad")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.cantidad)

        self.label_16 = QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.Cantidad = QTableWidget(self.genPedidos)
        self.Cantidad.setObjectName(u"Cantidad")
        self.Cantidad.setGeometry(QRect(20, 180, 391, 341))
        self.genInforme = QPushButton(self.genPedidos)
        self.genInforme.setObjectName(u"genInforme")
        self.genInforme.setGeometry(QRect(20, 120, 111, 24))
        self.hacerPedido = QPushButton(self.genPedidos)
        self.hacerPedido.setObjectName(u"hacerPedido")
        self.hacerPedido.setGeometry(QRect(20, 150, 111, 24))
        self.tabWidget.addTab(self.genPedidos, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addMueble.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir mueble", None))
        self.delMueble.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Eliminar mueble", None))
        self.modMueble.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Modificar mueble", None))
        self.listMuebles.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ListarMuebles", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Mueble", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Id mueble", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dimensiones", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Altura", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ancho", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Largo", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Dimensiones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gestMuebles), QCoreApplication.translate("MainWindow", u"Gestionar mubles", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Id Pedido", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"ID Mueble", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.genInforme.setText(QCoreApplication.translate("MainWindow", u"Generar Informe", None))
        self.hacerPedido.setText(QCoreApplication.translate("MainWindow", u"Hacer Pedido", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.genPedidos), QCoreApplication.translate("MainWindow", u"Generar pedidos", None))
    # retranslateUi


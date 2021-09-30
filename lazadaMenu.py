# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lazadaMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LazadaMenu(object):
    def setupUi(self, LazadaMenu):
        LazadaMenu.setObjectName("LazadaMenu")
        LazadaMenu.resize(800, 600)
        LazadaMenu.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(LazadaMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setMaximumSize(QtCore.QSize(800, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("background-color: rgb(0, 173, 239);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lblNama = QtWidgets.QLabel(self.widget)
        self.lblNama.setGeometry(QtCore.QRect(110, 25, 691, 31))
        self.lblNama.setStyleSheet("font-size:14px;\n"
"font-weight:350;")
        self.lblNama.setObjectName("lblNama")
        self.lblSubsribe = QtWidgets.QLabel(self.widget)
        self.lblSubsribe.setGeometry(QtCore.QRect(110, 80, 691, 31))
        self.lblSubsribe.setStyleSheet("font-size:14px;\n"
"font-weight:250;")
        self.lblSubsribe.setObjectName("lblSubsribe")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:1px solid white;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 350, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtItem = QtWidgets.QPlainTextEdit(self.widget)
        self.txtItem.setGeometry(QtCore.QRect(10, 210, 641, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtItem.setFont(font)
        self.txtItem.setObjectName("txtItem")
        self.txtPage = QtWidgets.QPlainTextEdit(self.widget)
        self.txtPage.setGeometry(QtCore.QRect(10, 380, 641, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPage.setFont(font)
        self.txtPage.setObjectName("txtPage")
        self.btnItem = QtWidgets.QPushButton(self.widget)
        self.btnItem.setGeometry(QtCore.QRect(660, 210, 131, 131))
        self.btnItem.setStyleSheet("font-size:18px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:none;\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:25px;\n"
"")
        self.btnItem.setObjectName("btnItem")
        self.btnPage = QtWidgets.QPushButton(self.widget)
        self.btnPage.setGeometry(QtCore.QRect(660, 380, 131, 131))
        self.btnPage.setStyleSheet("font-size:18px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:none;\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:25px;\n"
"")
        self.btnPage.setObjectName("btnPage")
        self.btnBack = QtWidgets.QPushButton(self.widget)
        self.btnBack.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.btnBack.setObjectName("btnBack")
        LazadaMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LazadaMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        LazadaMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LazadaMenu)
        self.statusbar.setObjectName("statusbar")
        LazadaMenu.setStatusBar(self.statusbar)

        self.retranslateUi(LazadaMenu)
        QtCore.QMetaObject.connectSlotsByName(LazadaMenu)

    def retranslateUi(self, LazadaMenu):
        _translate = QtCore.QCoreApplication.translate
        LazadaMenu.setWindowTitle(_translate("LazadaMenu", "SIMAKET"))
        self.lblNama.setText(_translate("LazadaMenu", "Ini Nama Login User"))
        self.lblSubsribe.setText(_translate("LazadaMenu", "Anda berlangganan Aplikasi Ini mulai tanggal dd-mm-yyyy hingga dd-mm-yyyy"))
        self.label_2.setText(_translate("LazadaMenu", "ini Logo Nantinya"))
        self.label_3.setText(_translate("LazadaMenu", "Scrap per Item"))
        self.label_4.setText(_translate("LazadaMenu", "Scrap per Page"))
        self.btnItem.setText(_translate("LazadaMenu", "Scrap Item"))
        self.btnPage.setText(_translate("LazadaMenu", "Scrap Shop"))
        self.btnBack.setText(_translate("LazadaMenu", "back to menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LazadaMenu = QtWidgets.QMainWindow()
    ui = Ui_LazadaMenu()
    ui.setupUi(LazadaMenu)
    LazadaMenu.show()
    sys.exit(app.exec_())

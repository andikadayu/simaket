# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShopeeMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from models.activateHelper import activateHelper
from models.databaseLite import databaseLite

from models.shopeePage import shopeePage
from models.shopeeDetail import shopeeDetail
from datetime import datetime


class Ui_ShopeeMenu(object):
    def setupUi(self, ShopeeMenu):
        ShopeeMenu.setObjectName("ShopeeMenu")
        ShopeeMenu.resize(800, 600)
        ShopeeMenu.setMinimumSize(QtCore.QSize(800, 600))
        ShopeeMenu.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(ShopeeMenu)
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
        self.txtShop = QtWidgets.QPlainTextEdit(self.widget)
        self.txtShop.setGeometry(QtCore.QRect(10, 380, 641, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtShop.setFont(font)
        self.txtShop.setObjectName("txtShop")
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
        self.btnShop = QtWidgets.QPushButton(self.widget)
        self.btnShop.setGeometry(QtCore.QRect(660, 380, 131, 131))
        self.btnShop.setStyleSheet("font-size:18px;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "border:none;\n"
                                   "color:white;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:25px;\n"
                                   "")
        self.btnShop.setObjectName("btnShop")
        self.btnBack = QtWidgets.QPushButton(self.widget)
        self.btnBack.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.btnBack.setObjectName("btnBack")
        ShopeeMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShopeeMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ShopeeMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ShopeeMenu)
        self.statusbar.setObjectName("statusbar")
        ShopeeMenu.setStatusBar(self.statusbar)

        self.retranslateUi(ShopeeMenu)
        QtCore.QMetaObject.connectSlotsByName(ShopeeMenu)

        # button action handle
        self.btnItem.clicked.connect(self.itemAction)
        self.btnShop.clicked.connect(self.shopAction)
        self.btnBack.clicked.connect(self.backMenu)

    def retranslateUi(self, ShopeeMenu):
        _translate = QtCore.QCoreApplication.translate
        ShopeeMenu.setWindowTitle(_translate("ShopeeMenu", "SIMAKET"))
        self.lblNama.setText(_translate("ShopeeMenu", self.getName()))
        self.lblSubsribe.setText(_translate(
            "ShopeeMenu", self.getActivate()))
        self.label_2.setText(_translate("ShopeeMenu", "ini Logo Nantinya"))
        self.label_3.setText(_translate("ShopeeMenu", "Scrap per Item"))
        self.label_4.setText(_translate("ShopeeMenu", "Scrap per Shop"))
        self.btnItem.setText(_translate("ShopeeMenu", "Scrap Item"))
        self.btnShop.setText(_translate("ShopeeMenu", "Scrap Shop"))
        self.btnBack.setText(_translate("ShopeeMenu", "back to menu"))

    def getActivate(self):
        activHelp = activateHelper()
        stats = activHelp.getActivate()
        if stats['active_status'] == 'OK':
            return stats['active_text']
        else:
            self.hasErrorActivate(stats['active_text'])
            return stats['active_text']

    def hasErrorActivate(self, text):
        lin = QtWidgets.QMessageBox(self.centralwidget)
        lin.setText(text)
        lin.exec()

    def getName(self):
        activHelp = activateHelper()
        return activHelp.getName()

    def itemAction(self):
        ids = 0
        links = self.txtItem.toPlainText()
        datenow = str(datetime.date(datetime.now()))
        if links == '':
            lin = QtWidgets.QMessageBox(self.centralwidget)
            lin.setText('Complete the form')
            lin.exec()
        else:
            alllink = links.split(',')
            dblite = databaseLite()
            ids = dblite.insert_getId('tb_scrap', "(NULL,'"+datenow+"','1')")
            for ans in alllink:
                shopee = shopeeDetail(str(ans))
                shopee.getData(ids)

            linz = QtWidgets.QMessageBox(self.centralwidget)
            linz.setText('Done')
            linz.exec()
            self.txtItem.setPlainText("")

    def shopAction(self):
        ids = 0
        links = self.txtShop.toPlainText()
        getlink = []
        datenow = str(datetime.date(datetime.now()))

        if links == '':
            lin = QtWidgets.QMessageBox(self.centralwidget)
            lin.setText('Complete the form')
            lin.exec()
        else:
            allLink = links.split(',')
            dblite = databaseLite()
            ids = dblite.insert_getId('tb_scrap', "(NULL,'"+datenow+"','1')")
            for lins in allLink:
                shopees = shopeePage(lins)
                numbers = shopees.getMaxPage()
                getlink = shopees.getAllUrl(int(numbers))

                for ans in getlink:
                    detail = shopeeDetail(str(ans))
                    detail.getData(ids)

                getlink = []
                # shopees.shutDown()

            linz = QtWidgets.QMessageBox(self.centralwidget)
            linz.setText('Done')
            linz.exec()
            self.txtShop.setPlainText("")

    def backMenu(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShopeeMenu = QtWidgets.QMainWindow()
    ui = Ui_ShopeeMenu()
    ui.setupUi(ShopeeMenu)
    ShopeeMenu.show()
    sys.exit(app.exec_())

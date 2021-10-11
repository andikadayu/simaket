# PYQT5 LIBRARY
from PyQt5 import QtCore, QtGui, QtWidgets

# OTHER LIBRARY
import requests
import yaml
from pathlib import Path
from datetime import datetime
import json

# CUSTOM LIBRARY
from models.activateHelper import activateHelper
from models.databaseLite import databaseLite
from models.shopeePage import shopeePage
from models.shopeeDetail import shopeeDetail
from models.lazadaDetail import lazadaDetail
from models.lazadaItem import lazadaItem
from models.lazadaPage import lazadaPage
from models.excelCreate import excelcreate

# LOGIN SECTION


class LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(800, 600)
        LoginPage.setMinimumSize(QtCore.QSize(800, 600))
        LoginPage.setMaximumSize(QtCore.QSize(800, 600))
        LoginPage.setAutoFillBackground(True)
        LoginPage.setWindowIcon(
            QtGui.QIcon("assets/standalone.png"))
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("background-color: rgb(204, 242, 244);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textTitle = QtWidgets.QLabel(self.widget)
        self.textTitle.setGeometry(QtCore.QRect(330, 20, 131, 91))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.textTitle.setFont(font)

        self.textTitle.setObjectName("textTitle")
        self.textLogin = QtWidgets.QLabel(self.widget)
        self.textLogin.setGeometry(QtCore.QRect(220, 85, 355, 61))
        self.textLogin.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textLogin.setFont(font)
        self.textLogin.setStyleSheet("color: rgb(0, 0, 0);")
        self.textLogin.setObjectName("textLogin")
        self.textLogin_2 = QtWidgets.QLabel(self.widget)
        self.textLogin_2.setGeometry(QtCore.QRect(40, 150, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textLogin_2.setFont(font)
        self.textLogin_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.textLogin_2.setObjectName("textLogin_2")
        self.txtEmail = QtWidgets.QLineEdit(self.widget)
        self.txtEmail.setGeometry(QtCore.QRect(40, 210, 741, 51))
        self.txtEmail.setStyleSheet("background-color: rgb(204, 242, 244);\n"
                                    "border:none;\n"
                                    "border-bottom: 2px solid rgb(0, 0, 0);\n"
                                    "color:rgb(0,0,0);\n"
                                    "padding-bottom:7px;\n"
                                    "font-size:14px;")
        self.txtEmail.setObjectName("txtEmail")
        self.txtPassword = QtWidgets.QLineEdit(self.widget)
        self.txtPassword.setGeometry(QtCore.QRect(40, 340, 741, 51))
        self.txtPassword.setStyleSheet("background-color: rgb(204, 242, 244);\n"
                                       "border:none;\n"
                                       "border-bottom: 2px solid rgb(0, 0, 0);\n"
                                       "color:rgb(0,0,0);\n"
                                       "padding-bottom:7px;\n"
                                       "font-size:14px;")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.textLogin_3 = QtWidgets.QLabel(self.widget)
        self.textLogin_3.setGeometry(QtCore.QRect(40, 280, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textLogin_3.setFont(font)
        self.textLogin_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.textLogin_3.setObjectName("textLogin_3")
        self.btnLogin = QtWidgets.QPushButton(self.widget)
        self.btnLogin.setGeometry(QtCore.QRect(600, 460, 131, 51))

        self.btnLogin.setObjectName("btnLogin")
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

        # Button Icon
        self.btnLogin.setIcon(QtGui.QIcon('assets/login.png'))
        self.btnLogin.setIconSize(QtCore.QSize(48, 48))
        self.btnLogin.setStyleSheet("font-size:18px;\n"
                                    "background-color: rgb(110, 203, 99);\n"
                                    "border:none;\n"
                                    "color:black;\n"
                                    "font-weight:bold;\n"
                                    "margin-left:5px;\n"
                                    "border-radius:10px;")

        self.textTitle.setPixmap(QtGui.QPixmap("assets/standalone.png"))
        self.textTitle.setScaledContents(True)

        # for handle action button
        self.btnLogin.clicked.connect(self.loginAction)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "SIMAKET"))
        self.textTitle.setText(_translate("LoginPage", "SIMAKET"))
        self.textLogin.setText(_translate(
            "LoginPage", "SIMAKET\nAplikasi Optimalisasi Marketplace"))
        self.textLogin_2.setText(_translate("LoginPage", "Email"))
        self.textLogin_3.setText(_translate("LoginPage", "Password"))
        self.btnLogin.setText(_translate("LoginPage", "Login"))

    def loginAction(self):
        emails = self.txtEmail.text()
        passwords = self.txtPassword.text()

        if emails == '' or passwords == '':
            lin = QtWidgets.QMessageBox.warning(
                self.centralwidget, "SIMAKET", "Complete the form")
        else:
            hostlink = "https://marketing.pt-ckit.com/api/login_apps.php"
            datas = {'email': emails, 'password': passwords}

            try:
                resp = requests.post(hostlink, data=datas, timeout=None)
                retcode = resp.json()

                if(retcode['status'] == 'OK'):
                    with open(str(Path().absolute())+'/config/config.yaml', 'w') as f:
                        yaml.dump(retcode, f)
                    lin = QtWidgets.QMessageBox.information(
                        self.centralwidget, "SIMAKET", "Login Success")

                    Main_Window.close()

                    IndexView.setupUi(Main_Window)
                    Main_Window.show()

                else:
                    lin = QtWidgets.QMessageBox(self.centralwidget)
                    lin.setText('Email/Password Incorrect')
                    lin.exec()

            except requests.ConnectionError as error:
                lines = QtWidgets.QMessageBox(self.MainWindow)
                lines.setText(error)
                lines.exec()


# INDEX SECTION

class indexMenu(object):
    def setupUi(self, indexMenu):
        indexMenu.setObjectName("indexMenu")
        indexMenu.resize(800, 600)
        indexMenu.setMinimumSize(QtCore.QSize(800, 600))
        indexMenu.setMaximumSize(QtCore.QSize(800, 600))
        indexMenu.setWindowIcon(
            QtGui.QIcon("assets/standalone.png"))
        self.centralwidget = QtWidgets.QWidget(indexMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 800, 600))
        self.widget.setMaximumSize(QtCore.QSize(800, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("background-color: rgb(204, 242, 244);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:1px solid white; padding-top:10px;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
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
        self.btnShopee = QtWidgets.QPushButton(self.widget)
        self.btnShopee.setGeometry(QtCore.QRect(50, 200, 120, 120))
        self.btnShopee.setObjectName("btnShopee")
        self.btnLazada = QtWidgets.QPushButton(self.widget)
        self.btnLazada.setGeometry(QtCore.QRect(50, 380, 120, 120))
        self.btnLazada.setObjectName("btnLazada")
        self.btnTampil = QtWidgets.QPushButton(self.widget)
        self.btnTampil.setGeometry(QtCore.QRect(410, 200, 120, 120))
        self.btnTampil.setObjectName("btnTampil")
        self.btnExport = QtWidgets.QPushButton(self.widget)
        self.btnExport.setGeometry(QtCore.QRect(410, 380, 120, 120))
        self.btnExport.setObjectName("btnExport")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(180, 230, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(180, 410, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(550, 230, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(550, 410, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btnLogout = QtWidgets.QPushButton(self.widget)
        self.btnLogout.setGeometry(QtCore.QRect(660, 520, 131, 51))
        self.btnLogout.setObjectName("btnLogout")
        indexMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(indexMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        indexMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(indexMenu)
        self.statusbar.setObjectName("statusbar")
        indexMenu.setStatusBar(self.statusbar)

        self.retranslateUi(indexMenu)
        QtCore.QMetaObject.connectSlotsByName(indexMenu)

        # Button Icon
        self.btnLazada.setIcon(QtGui.QIcon('assets/lazadascrap.png'))
        self.btnLazada.setIconSize(QtCore.QSize(120, 120))
        self.btnLazada.setStyleSheet("border:none")

        self.btnShopee.setIcon(QtGui.QIcon('assets/shopeescrap.png'))
        self.btnShopee.setIconSize(QtCore.QSize(120, 120))
        self.btnShopee.setStyleSheet("border:none")

        self.btnTampil.setIcon(QtGui.QIcon('assets/frequency.png'))
        self.btnTampil.setIconSize(QtCore.QSize(120, 120))
        self.btnTampil.setStyleSheet("border:none")

        self.btnExport.setIcon(QtGui.QIcon('assets/excel.png'))
        self.btnExport.setIconSize(QtCore.QSize(120, 120))
        self.btnExport.setStyleSheet("border:none")

        self.btnLogout.setIcon(QtGui.QIcon('assets/logout.png'))
        self.btnLogout.setIconSize(QtCore.QSize(48, 48))
        self.btnLogout.setStyleSheet("font-size:18px;\n"
                                     "background-color: rgb(110, 203, 99);\n"
                                     "border:none;\n"
                                     "color:black;\n"
                                     "font-weight:bold;\n"
                                     "margin-left:5px;\n"
                                     "border-radius:10px;")

        self.setHeader()

        # Button Handle Action
        self.btnExport.clicked.connect(self.toExport)
        self.btnLazada.clicked.connect(self.toLazada)
        self.btnShopee.clicked.connect(self.toShopee)
        self.btnTampil.clicked.connect(self.toTampil)
        self.btnLogout.clicked.connect(self.LogoutAction)

    def retranslateUi(self, indexMenu):
        _translate = QtCore.QCoreApplication.translate
        indexMenu.setWindowTitle(_translate("indexMenu", "SIMAKET"))
        self.label_2.setText(_translate("indexMenu", "ini Logo Nantinya"))
        self.lblNama.setText(_translate("indexMenu", self.getName()))
        self.lblSubsribe.setText(_translate(
            "indexMenu", self.getActivate()))
        self.label_3.setText(_translate("indexMenu", "Shopee Scrapper"))
        self.label_4.setText(_translate("indexMenu", "Lazada Scrapper"))
        self.label_5.setText(_translate("indexMenu", "Tampil Data"))
        self.label_6.setText(_translate("indexMenu", "Export Excel"))
        self.btnLogout.setText(_translate("indexMenu", "Logout"))

    def setHeader(self):
        self.label_2.setPixmap(QtGui.QPixmap("assets/standalone.png"))
        self.label_2.setScaledContents(True)

    def getActivate(self):
        activHelp = activateHelper()
        stats = activHelp.getActivate()
        if stats['active_status'] == 'OK':
            return stats['active_text']
        else:
            self.hasErrorActivate(stats['active_text'])
            return stats['active_text']

    def hasErrorActivate(self, text):
        lin = QtWidgets.QMessageBox.warning(
            self.centralwidget, "SIMAKET", text)
        self.LogoutAction()

    def getName(self):
        activHelp = activateHelper()
        return activHelp.getName()

    def toShopee(self):
        Main_Window.close()
        ShopeeView.setupUi(Main_Window)
        Main_Window.show()

    def toLazada(self):
        Main_Window.close()
        LazadaView.setupUi(Main_Window)
        Main_Window.show()

    def toTampil(self):
        Main_Window.close()
        ViewView.setupUi(Main_Window)
        Main_Window.show()

    def toExport(self):
        Main_Window.close()
        ExportView.setupUi(Main_Window)
        Main_Window.show()

    def LogoutAction(self):
        retcode = {'email': 'ERROR', 'name': 'ERROR', 'status': 'ERROR'}
        with open(str(Path().absolute())+'/config/config.yaml', 'w') as f:
            yaml.dump(retcode, f)
        Main_Window.close()
        LoginView.setupUi(Main_Window)
        Main_Window.show()

# SHOPEE SECTION


class ShopeeMenu(object):
    def setupUi(self, ShopeeMenu):
        ShopeeMenu.setObjectName("ShopeeMenu")
        ShopeeMenu.resize(800, 600)
        ShopeeMenu.setMinimumSize(QtCore.QSize(800, 600))
        ShopeeMenu.setMaximumSize(QtCore.QSize(800, 600))
        ShopeeMenu.setWindowIcon(
            QtGui.QIcon("assets/standalone.png"))
        self.centralwidget = QtWidgets.QWidget(ShopeeMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setMaximumSize(QtCore.QSize(800, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("background-color: rgb(204, 242, 244);")
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
        self.label_2.setStyleSheet("border:1px solid white;padding-top:10px;")
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
        self.btnItem.setGeometry(QtCore.QRect(660, 220, 120, 95))

        self.btnItem.setObjectName("btnItem")
        self.btnShop = QtWidgets.QPushButton(self.widget)
        self.btnShop.setGeometry(QtCore.QRect(660, 390, 120, 95))

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

        self.setHeader()

        # Button Styling
        self.btnBack.setIcon(QtGui.QIcon('assets/back.png'))
        self.btnBack.setIconSize(QtCore.QSize(32, 32))
        self.btnBack.setStyleSheet("border:none;font-weight:bold;")

        self.btnShop.setIcon(QtGui.QIcon('assets/web-crawler.png'))
        self.btnShop.setIconSize(QtCore.QSize(64, 64))
        self.btnShop.setStyleSheet("font-size:18px;\n"
                                   "background-color: rgb(110, 203, 99);\n"
                                   "border:none;\n"
                                   "color:white;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:25px;\n"
                                   "")

        self.btnItem.setIcon(QtGui.QIcon('assets/web-crawler.png'))
        self.btnItem.setIconSize(QtCore.QSize(64, 64))
        self.btnItem.setStyleSheet("font-size:18px;\n"
                                   "background-color: rgb(110, 203, 99);\n"
                                   "border:none;\n"
                                   "color:white;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:25px;\n"
                                   "")

        # button action handle
        self.btnItem.clicked.connect(self.itemAction)
        self.btnShop.clicked.connect(self.shopAction)
        self.btnBack.clicked.connect(self.backMenu)

    def retranslateUi(self, ShopeeMenu):
        _translate = QtCore.QCoreApplication.translate
        ShopeeMenu.setWindowTitle(_translate(
            "ShopeeMenu", "SIMAKET - Shopee Menu"))
        self.lblNama.setText(_translate("ShopeeMenu", self.getName()))
        self.lblSubsribe.setText(_translate(
            "ShopeeMenu", self.getActivate()))
        self.label_2.setText(_translate("ShopeeMenu", "ini Logo Nantinya"))
        self.label_3.setText(_translate("ShopeeMenu", "Scrap per Item"))
        self.label_4.setText(_translate("ShopeeMenu", "Scrap per Shop"))
        self.btnItem.setText(_translate("ShopeeMenu", "Item"))
        self.btnShop.setText(_translate("ShopeeMenu", "Shop"))
        self.btnBack.setText(_translate("ShopeeMenu", "BACK"))

    def setHeader(self):
        self.label_2.setPixmap(QtGui.QPixmap("assets/standalone.png"))
        self.label_2.setScaledContents(True)

    def getActivate(self):
        activHelp = activateHelper()
        stats = activHelp.getActivate()
        if stats['active_status'] == 'OK':
            return stats['active_text']
        else:
            self.hasErrorActivate(stats['active_text'])
            return stats['active_text']

    def hasErrorActivate(self, text):
        lin = QtWidgets.QMessageBox.warning(
            self.centralwidget, "SIMAKET", text)
        self.LogoutAction()

    def getName(self):
        activHelp = activateHelper()
        return activHelp.getName()

    def itemAction(self):
        ids = 0
        links = self.txtItem.toPlainText()
        datenow = str(datetime.date(datetime.now()))
        if links == '':
            lin = QtWidgets.QMessageBox.warning(
                self.centralwidget, "SIMAKET", "Complete the form")
        else:
            alllink = links.split(',')
            dblite = databaseLite()
            ids = dblite.insert_getId('tb_scrap', "(NULL,'"+datenow+"','1')")
            for ans in alllink:
                shopee = shopeeDetail(str(ans))
                shopee.getData(ids)

            linz = QtWidgets.QMessageBox.information(
                self.centralwidget, "SIMAKET", "Done")
            self.txtItem.setPlainText("")

    def shopAction(self):
        ids = 0
        links = self.txtShop.toPlainText()
        getlink = []
        datenow = str(datetime.date(datetime.now()))

        if links == '':
            lin = QtWidgets.QMessageBox.warning(
                self.centralwidget, "SIMAKET", "Complete the form")
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
                shopees.shutDown()

            linz = QtWidgets.QMessageBox.information(
                self.centralwidget, "SIMAKET", "Done")
            self.txtShop.setPlainText("")

    def backMenu(self):
        Main_Window.close()
        IndexView.setupUi(Main_Window)
        Main_Window.show()

    def LogoutAction(self):
        retcode = {'email': 'ERROR', 'name': 'ERROR', 'status': 'ERROR'}
        with open(str(Path().absolute())+'/config/config.yaml', 'w') as f:
            yaml.dump(retcode, f)
        Main_Window.close()
        LoginView.setupUi(Main_Window)
        Main_Window.show()

# LAZADA SECTION


class LazadaMenu(object):
    def setupUi(self, LazadaMenu):
        LazadaMenu.setObjectName("LazadaMenu")
        LazadaMenu.resize(800, 600)
        LazadaMenu.setMinimumSize(QtCore.QSize(800, 600))
        LazadaMenu.setMaximumSize(QtCore.QSize(800, 600))
        LazadaMenu.setWindowIcon(
            QtGui.QIcon("assets/standalone.png"))
        self.centralwidget = QtWidgets.QWidget(LazadaMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setMaximumSize(QtCore.QSize(800, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("background-color: rgb(204, 242, 244);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lblNama = QtWidgets.QLabel(self.widget)
        self.lblNama.setGeometry(QtCore.QRect(110, 25, 691, 31))
        self.lblNama.setStyleSheet("font-size:14px;font-weight:350;")
        self.lblNama.setObjectName("lblNama")
        self.lblSubsribe = QtWidgets.QLabel(self.widget)
        self.lblSubsribe.setGeometry(QtCore.QRect(110, 80, 691, 31))
        self.lblSubsribe.setStyleSheet("font-size:14px;font-weight:250;")
        self.lblSubsribe.setObjectName("lblSubsribe")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:1px solid white;padding-top:10px;")
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
        self.btnItem.setGeometry(QtCore.QRect(660, 220, 120, 95))
        self.btnItem.setObjectName("btnItem")
        self.btnPage = QtWidgets.QPushButton(self.widget)
        self.btnPage.setGeometry(QtCore.QRect(660, 390, 120, 95))
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

        # Button Styling
        self.btnBack.setIcon(QtGui.QIcon('assets/back.png'))
        self.btnBack.setIconSize(QtCore.QSize(32, 32))
        self.btnBack.setStyleSheet("border:none;font-weight:bold;")

        self.btnPage.setIcon(QtGui.QIcon('assets/web-crawler.png'))
        self.btnPage.setIconSize(QtCore.QSize(64, 64))
        self.btnPage.setStyleSheet("font-size:18px;\n"
                                   "background-color: rgb(110, 203, 99);\n"
                                   "border:none;\n"
                                   "color:white;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:25px;\n"
                                   "")

        self.btnItem.setIcon(QtGui.QIcon('assets/web-crawler.png'))
        self.btnItem.setIconSize(QtCore.QSize(64, 64))
        self.btnItem.setStyleSheet("font-size:18px;\n"
                                   "background-color: rgb(110, 203, 99);\n"
                                   "border:none;\n"
                                   "color:white;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:25px;\n"
                                   "")

        self.setHeader()

        self.retranslateUi(LazadaMenu)
        QtCore.QMetaObject.connectSlotsByName(LazadaMenu)

        # button action handle
        self.btnItem.clicked.connect(self.itemAction)
        self.btnPage.clicked.connect(self.pageAction)
        self.btnBack.clicked.connect(self.backMenu)

    def retranslateUi(self, LazadaMenu):
        _translate = QtCore.QCoreApplication.translate
        LazadaMenu.setWindowTitle(_translate(
            "LazadaMenu", "SIMAKET - Lazada Menu"))
        self.lblNama.setText(_translate("LazadaMenu", self.getName()))
        self.lblSubsribe.setText(_translate(
            "LazadaMenu", self.getActivate()))
        # self.label_2.setText(_translate("LazadaMenu", "ini Logo Nantinya"))
        self.label_3.setText(_translate("LazadaMenu", "Scrap per Item"))
        self.label_4.setText(_translate("LazadaMenu", "Scrap per Page"))
        self.btnItem.setText(_translate("LazadaMenu", "Item"))
        self.btnPage.setText(_translate("LazadaMenu", "Page"))
        self.btnBack.setText(_translate("LazadaMenu", "BACK"))

    def setHeader(self):
        self.label_2.setPixmap(QtGui.QPixmap("assets/standalone.png"))
        self.label_2.setScaledContents(True)

    def getActivate(self):
        activHelp = activateHelper()
        stats = activHelp.getActivate()
        if stats['active_status'] == 'OK':
            return stats['active_text']
        else:
            self.hasErrorActivate(stats['active_text'])
            return stats['active_text']

    def hasErrorActivate(self, text):
        lin = QtWidgets.QMessageBox.warning(
            self.centralwidget, "SIMAKET", text)
        self.LogoutAction()

    def getName(self):
        activHelp = activateHelper()
        return activHelp.getName()

    def itemAction(self):
        ids = 0
        links = self.txtItem.toPlainText()
        datenow = str(datetime.date(datetime.now()))
        if links == '':
            lins = QtWidgets.QMessageBox.warning(
                self.centralwidget, "SIMAKET", "Complete the form")
        else:
            dblite = databaseLite()
            ids = dblite.insert_getId("tb_scrap", "(NULL,'"+datenow+"','2')")
            alllinks = links.split(',')
            for lin in alllinks:
                lazitem = lazadaItem(lin)
                jsdata = lazitem.getData()
                jsimage = json.dumps(lazitem.getImage())
                lazdet = lazadaDetail(lin)
                lazdet.getData(jsdata, jsimage, ids)
                lazitem.shutDown()

            linz = QtWidgets.QMessageBox.information(
                self.centralwidget, "SIMAKET", "Done")
            self.txtItem.setPlainText("")

    def pageAction(self):
        ids = 0
        links = self.txtPage.toPlainText()
        datenow = str(datetime.date(datetime.now()))
        link1 = []
        if links == '':
            lins = QtWidgets.QMessageBox.warning(
                self.centralwidget, "SIMAKET", "Complete the form")
        else:
            dblite = databaseLite()
            ids = dblite.insert_getId("tb_scrap", "(NULL,'"+datenow+"','2')")
            alllinks = links.split(',')
            for allsa in alllinks:
                lazap = lazadaPage(allsa)
                link1.append(lazap.getPage())
                lazap.shutDown()

            for sas in link1:
                for shine in sas:
                    lazitem = lazadaItem(shine)
                    jsdata = lazitem.getData()
                    jsimage = json.dumps(lazitem.getImage())
                    lazdet = lazadaDetail(shine)
                    lazdet.getData(jsdata, jsimage, ids)
                    lazitem.shutDown()

            linz = QtWidgets.QMessageBox.information(
                self.centralwidget, "SIMAKET", "Done")
            self.txtPage.setPlainText("")

    def backMenu(self):
        Main_Window.close()
        IndexView.setupUi(Main_Window)
        Main_Window.show()

    def LogoutAction(self):
        retcode = {'email': 'ERROR', 'name': 'ERROR', 'status': 'ERROR'}
        with open(str(Path().absolute())+'/config/config.yaml', 'w') as f:
            yaml.dump(retcode, f)
        Main_Window.close()
        LoginView.setupUi(Main_Window)
        Main_Window.show()

# VIEW SECTION


class ViewMenu(object):
    def setupUi(self, ViewMenu):
        ViewMenu.setObjectName("ViewMenu")
        ViewMenu.resize(800, 600)
        ViewMenu.setMinimumSize(QtCore.QSize(800, 600))
        ViewMenu.setMaximumSize(QtCore.QSize(800, 600))
        ViewMenu.setWindowIcon(
            QtGui.QIcon("assets/standalone.png"))
        self.centralwidget = QtWidgets.QWidget(ViewMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setMinimumSize(QtCore.QSize(800, 600))
        self.widget.setMaximumSize(QtCore.QSize(800, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setMinimumSize(QtCore.QSize(800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("background-color: rgb(204, 242, 244);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:1px solid white;padding-top:10px;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.lblNama = QtWidgets.QLabel(self.widget)
        self.lblNama.setGeometry(QtCore.QRect(110, 15, 691, 31))
        self.lblNama.setStyleSheet("font-size:14px;\n"
                                   "font-weight:350;")
        self.lblNama.setObjectName("lblNama")
        self.lblSubsribe = QtWidgets.QLabel(self.widget)
        self.lblSubsribe.setGeometry(QtCore.QRect(110, 70, 691, 31))
        self.lblSubsribe.setStyleSheet("font-size:14px;\n"
                                       "font-weight:250;")
        self.lblSubsribe.setObjectName("lblSubsribe")
        self.btnBack = QtWidgets.QPushButton(self.widget)
        self.btnBack.setGeometry(QtCore.QRect(10, 120, 121, 31))
        self.btnBack.setObjectName("btnBack")
        self.tableView = QtWidgets.QTableWidget(self.widget)
        self.tableView.setGeometry(QtCore.QRect(20, 230, 750, 280))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tableView.setFont(font)
        self.tableView.setAutoFillBackground(False)
        self.tableView.setStyleSheet("")
        self.tableView.setFrameShape(QtWidgets.QFrame.HLine)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(2, item)
        self.tableView.horizontalHeader().setDefaultSectionSize(242)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.btnRefresh = QtWidgets.QPushButton(self.widget)
        self.btnRefresh.setGeometry(QtCore.QRect(20, 180, 121, 31))
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnDelete = QtWidgets.QPushButton(self.widget)
        self.btnDelete.setGeometry(QtCore.QRect(650, 180, 121, 31))
        self.btnDelete.setObjectName("btnDelete")
        ViewMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ViewMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewMenu)
        self.statusbar.setObjectName("statusbar")
        ViewMenu.setStatusBar(self.statusbar)

        self.retranslateUi(ViewMenu)
        QtCore.QMetaObject.connectSlotsByName(ViewMenu)

        self.setHeader()

        # Button Styling
        self.btnBack.setIcon(QtGui.QIcon('assets/back.png'))
        self.btnBack.setIconSize(QtCore.QSize(32, 32))
        self.btnBack.setStyleSheet("border:none;font-weight:bold;")

        self.btnRefresh.setIcon(QtGui.QIcon('assets/refresh.png'))
        self.btnRefresh.setIconSize(QtCore.QSize(32, 32))
        self.btnRefresh.setStyleSheet("border:none;font-weight:bold;")

        self.btnDelete.setIcon(QtGui.QIcon('assets/delete.png'))
        self.btnDelete.setIconSize(QtCore.QSize(32, 32))
        self.btnDelete.setStyleSheet("border:none;font-weight:bold;")

        # First Load All Data
        self.loadAllData()

        # action button handle
        self.btnBack.clicked.connect(self.backMenu)
        self.btnRefresh.clicked.connect(self.loadAllData)
        self.btnDelete.clicked.connect(self.deleteAllData)

    def retranslateUi(self, ViewMenu):
        _translate = QtCore.QCoreApplication.translate
        ViewMenu.setWindowTitle(_translate("ViewMenu", "SIMAKET"))
        self.label_2.setText(_translate("ViewMenu", "ini Logo Nantinya"))
        self.lblNama.setText(_translate("ViewMenu", self.getName()))
        self.lblSubsribe.setText(_translate("ViewMenu", self.getActivate()))
        item = self.tableView.horizontalHeaderItem(0)
        item.setText(_translate("ViewMenu", "Commerce"))
        item = self.tableView.horizontalHeaderItem(1)
        item.setText(_translate("ViewMenu", "Tanggal"))
        item = self.tableView.horizontalHeaderItem(2)
        item.setText(_translate("ViewMenu", "Jumlah"))
        self.btnBack.setText(_translate("ViewMenu", "BACK"))
        self.btnRefresh.setText(_translate("ViewMenu", "REFRESH"))
        self.btnDelete.setText(_translate("ViewMenu", "DELETE ALL"))

    def setHeader(self):
        self.label_2.setPixmap(QtGui.QPixmap("assets/standalone.png"))
        self.label_2.setScaledContents(True)

    def getActivate(self):
        activHelp = activateHelper()
        stats = activHelp.getActivate()
        if stats['active_status'] == 'OK':
            return stats['active_text']
        else:
            self.hasErrorActivate(stats['active_text'])
            return stats['active_text']

    def hasErrorActivate(self, text):
        lin = QtWidgets.QMessageBox.warning(
            self.centralwidget, "SIMAKET", text)
        self.LogoutAction()

    def getName(self):
        activHelp = activateHelper()
        return activHelp.getName()

    def loadAllData(self):

        dblite = databaseLite()
        cts = dblite.get_count("tb_scrap", "id_scrap", "", "")
        self.tableView.setRowCount(cts)
        tbrow = 0
        rowalls = dblite.read_dateabase("tb_detail", "tb_commerce.name_commerce as commerce,tb_scrap.tgl_scrap as dates ,COUNT(tb_detail.id_detail) as counts",
                                        "INNER JOIN tb_scrap ON tb_scrap.id_scrap = tb_detail.id_scrape INNER JOIN tb_commerce ON tb_commerce.id_commerce = tb_scrap.id_commerce", "", "tb_detail.id_scrape", "tgl_scrap DESC", "50", "0")
        for row in rowalls:
            self.tableView.setItem(
                tbrow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableView.setItem(
                tbrow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableView.setItem(
                tbrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))

            tbrow += 1

    def deleteAllData(self):
        linz = QtWidgets.QMessageBox.question(self.centralwidget, "SIMAKET", "Are you sure to delete all data?",
                                              QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No)
        if linz == QtWidgets.QMessageBox.StandardButton.Yes:
            dblite = databaseLite()
            dblite.truncate_database()

            lin = QtWidgets.QMessageBox.information(
                self.centralwidget, "SIMAKET", "Delete All Data Done")
            self.loadAllData()

    def backMenu(self):
        Main_Window.close()
        IndexView.setupUi(Main_Window)
        Main_Window.show()

    def LogoutAction(self):
        retcode = {'email': 'ERROR', 'name': 'ERROR', 'status': 'ERROR'}
        with open(str(Path().absolute())+'/config/config.yaml', 'w') as f:
            yaml.dump(retcode, f)
        Main_Window.close()
        LoginView.setupUi(Main_Window)
        Main_Window.show()

# EXPORT ACTION


class ExportMenu(object):
    def setupUi(self, ExportMenu):
        ExportMenu.setObjectName("ExportMenu")
        ExportMenu.resize(800, 600)
        ExportMenu.setMinimumSize(QtCore.QSize(800, 600))
        ExportMenu.setMaximumSize(QtCore.QSize(800, 600))
        ExportMenu.setWindowIcon(
            QtGui.QIcon("assets/standalone.png"))
        self.centralwidget = QtWidgets.QWidget(ExportMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setMinimumSize(QtCore.QSize(800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("background-color: rgb(204, 242, 244);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lblSubsribe = QtWidgets.QLabel(self.widget)
        self.lblSubsribe.setGeometry(QtCore.QRect(110, 80, 691, 31))
        self.lblSubsribe.setStyleSheet("font-size:14px;\n"
                                       "font-weight:250;")
        self.lblSubsribe.setObjectName("lblSubsribe")
        self.btnBack = QtWidgets.QPushButton(self.widget)
        self.btnBack.setGeometry(QtCore.QRect(10, 130, 121, 31))
        self.btnBack.setObjectName("btnBack")
        self.lblNama = QtWidgets.QLabel(self.widget)
        self.lblNama.setGeometry(QtCore.QRect(110, 25, 691, 31))
        self.lblNama.setStyleSheet("font-size:14px;\n"
                                   "font-weight:350;")
        self.lblNama.setObjectName("lblNama")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:1px solid white;padding-top:10px;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cbCommerce = QtWidgets.QComboBox(self.widget)
        self.cbCommerce.setGeometry(QtCore.QRect(20, 220, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cbCommerce.setFont(font)
        self.cbCommerce.setObjectName("cbCommerce")
        self.cbCommerce.addItem("")
        self.cbCommerce.addItem("")
        self.txtPreorder = QtWidgets.QLineEdit(self.widget)
        self.txtPreorder.setGeometry(QtCore.QRect(280, 220, 181, 31))
        self.txtPreorder.setObjectName("txtPreorder")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(280, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtEtalase = QtWidgets.QLineEdit(self.widget)
        self.txtEtalase.setGeometry(QtCore.QRect(550, 220, 181, 31))
        self.txtEtalase.setObjectName("txtEtalase")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(550, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtKategori = QtWidgets.QLineEdit(self.widget)
        self.txtKategori.setGeometry(QtCore.QRect(20, 310, 181, 31))
        self.txtKategori.setObjectName("txtKategori")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(280, 270, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtMarkup = QtWidgets.QLineEdit(self.widget)
        self.txtMarkup.setGeometry(QtCore.QRect(280, 310, 181, 31))
        self.txtMarkup.setObjectName("txtMarkup")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(550, 270, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txtBerat = QtWidgets.QLineEdit(self.widget)
        self.txtBerat.setGeometry(QtCore.QRect(550, 310, 181, 31))
        self.txtBerat.setObjectName("txtBerat")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(20, 360, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txtMinPesan = QtWidgets.QLineEdit(self.widget)
        self.txtMinPesan.setGeometry(QtCore.QRect(20, 400, 181, 31))
        self.txtMinPesan.setObjectName("txtMinPesan")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.txtStok = QtWidgets.QLineEdit(self.widget)
        self.txtStok.setGeometry(QtCore.QRect(20, 490, 181, 31))
        self.txtStok.setObjectName("txtStok")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(280, 360, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txtHapus = QtWidgets.QPlainTextEdit(self.widget)
        self.txtHapus.setGeometry(QtCore.QRect(280, 400, 301, 131))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtHapus.setFont(font)
        self.txtHapus.setObjectName("txtHapus")
        self.btnExport = QtWidgets.QPushButton(self.widget)
        self.btnExport.setGeometry(QtCore.QRect(630, 480, 131, 51))

        self.btnExport.setObjectName("btnExport")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(440, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.txtNamaFile = QtWidgets.QLineEdit(self.widget)
        self.txtNamaFile.setGeometry(QtCore.QRect(550, 130, 181, 31))
        self.txtNamaFile.setObjectName("txtNamaFile")
        ExportMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExportMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ExportMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExportMenu)
        self.statusbar.setObjectName("statusbar")
        ExportMenu.setStatusBar(self.statusbar)

        self.retranslateUi(ExportMenu)
        QtCore.QMetaObject.connectSlotsByName(ExportMenu)

        self.setHeader()

        # Button Styling
        self.btnBack.setIcon(QtGui.QIcon('assets/back.png'))
        self.btnBack.setIconSize(QtCore.QSize(32, 32))
        self.btnBack.setStyleSheet("border:none;font-weight:bold;")

        self.btnExport.setIcon(QtGui.QIcon('assets/excel.png'))
        self.btnExport.setIconSize(QtCore.QSize(32, 32))
        self.btnExport.setStyleSheet("font-size:18px;\n"
                                     "background-color: rgb(110, 203, 99);\n"
                                     "border:none;\n"
                                     "color:black;\n"
                                     "font-weight:bold;\n"
                                     "margin-left:5px;\n"
                                     "border-radius:10px;")

        # Action Button Handle
        self.btnBack.clicked.connect(self.backMenu)
        self.btnExport.clicked.connect(self.exportAction)

    def retranslateUi(self, ExportMenu):
        _translate = QtCore.QCoreApplication.translate
        ExportMenu.setWindowTitle(_translate("ExportMenu", "SIMAKET"))
        self.lblSubsribe.setText(_translate(
            "ExportMenu", self.getActivate()))
        self.btnBack.setText(_translate("ExportMenu", "BACK"))
        self.lblNama.setText(_translate("ExportMenu", self.getName()))
        self.label_2.setText(_translate("ExportMenu", "ini Logo Nantinya"))
        self.label_3.setText(_translate("ExportMenu", "Commerce"))
        self.cbCommerce.setItemText(0, _translate("ExportMenu", "Shopee"))
        self.cbCommerce.setItemText(1, _translate("ExportMenu", "Lazada"))
        self.label_4.setText(_translate("ExportMenu", "Preorder*"))
        self.label_5.setText(_translate("ExportMenu", "Etalase"))
        self.label_6.setText(_translate("ExportMenu", "Kategori*"))
        self.label_7.setText(_translate("ExportMenu", "Markup (%)*"))
        self.label_8.setText(_translate("ExportMenu", "Berat (g)*"))
        self.label_9.setText(_translate("ExportMenu", "Min Pesan*"))
        self.label_10.setText(_translate("ExportMenu", "Stok*"))
        self.label_11.setText(_translate(
            "ExportMenu", "Hapus Kata"))
        self.btnExport.setText(_translate("ExportMenu", "Export"))
        self.label_12.setText(_translate("ExportMenu", "Nama File*"))

    def setHeader(self):
        self.label_2.setPixmap(QtGui.QPixmap("assets/standalone.png"))
        self.label_2.setScaledContents(True)

    def getActivate(self):
        activHelp = activateHelper()
        stats = activHelp.getActivate()
        if stats['active_status'] == 'OK':
            return stats['active_text']
        else:
            self.hasErrorActivate(stats['active_text'])
            return stats['active_text']

    def hasErrorActivate(self, text):
        lin = QtWidgets.QMessageBox.warning(
            self.centralwidget, "SIMAKET", text)
        self.LogoutAction()

    def getName(self):
        activHelp = activateHelper()
        return activHelp.getName()

    def exportAction(self):
        dblite = databaseLite()
        nama_file = self.txtNamaFile.text()
        commerce = self.cbCommerce.currentText()
        preorder = self.txtPreorder.text()
        etalase = self.txtEtalase.text()
        kategori = self.txtKategori.text()
        markup = self.txtMarkup.text()
        berat = self.txtBerat.text()
        min_pesan = self.txtMinPesan.text()
        stok = self.txtStok.text()
        hapus_kata = self.txtHapus.toPlainText()
        idc = 0
        if commerce == 'Shopee':
            idc = 1
        else:
            idc = 2

        if nama_file == '' or preorder == '' or kategori == '' or markup == '' or berat == '' or min_pesan == '' or stok == '':
            lin = QtWidgets.QMessageBox.warning(
                self.centralwidget, "SIMAKET", "Complete the form")
        else:
            counts = dblite.get_count("tb_detail", "tb_detail.id_detail",
                                      "INNER JOIN tb_scrap ON tb_scrap.id_scrap = tb_detail.id_scrape", "tb_scrap.id_commerce='"+str(idc)+"'")
            f = 0
            exportExcel = excelcreate()
            while(f < int(counts)):
                if f % 299 == 0:
                    exportExcel.create_excel(
                        "299", f, idc, nama_file, preorder, etalase, kategori, markup, berat, min_pesan, stok, hapus_kata)

                if f == int(counts) - 1:
                    lin = QtWidgets.QMessageBox.information(
                        self.centralwidget, "SIMAKET", "Done")

                f += 1

    def backMenu(self):
        Main_Window.close()
        IndexView.setupUi(Main_Window)
        Main_Window.show()

    def LogoutAction(self):
        retcode = {'email': 'ERROR', 'name': 'ERROR', 'status': 'ERROR'}
        with open(str(Path().absolute())+'/config/config.yaml', 'w') as f:
            yaml.dump(retcode, f)
        Main_Window.close()
        LoginView.setupUi(Main_Window)
        Main_Window.show()


# MAIN CODE
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = QtWidgets.QMainWindow()

    # DECLARE GLOBAL VIEW
    LoginView = LoginPage()
    IndexView = indexMenu()
    ShopeeView = ShopeeMenu()
    LazadaView = LazadaMenu()
    ViewView = ViewMenu()
    ExportView = ExportMenu()

    # INITIAL FIRST SHOW
    LoginView.setupUi(Main_Window)
    Main_Window.show()

    # DEFAULT
    sys.exit(app.exec_())

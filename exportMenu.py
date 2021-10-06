# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExportMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from models.activateHelper import activateHelper
from models.databaseLite import databaseLite
from models.excelCreate import excelcreate


class Ui_ExportMenu(object):
    def setupUi(self, ExportMenu):
        ExportMenu.setObjectName("ExportMenu")
        ExportMenu.resize(800, 600)
        ExportMenu.setMinimumSize(QtCore.QSize(800, 600))
        ExportMenu.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(ExportMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setMinimumSize(QtCore.QSize(800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("background-color: rgb(0, 173, 239);")
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
        self.label_2.setStyleSheet("border:1px solid white;")
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
        self.btnExport.setStyleSheet("font-size:18px;\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                     "border:none;\n"
                                     "color:white;\n"
                                     "font-weight:bold;\n"
                                     "border-radius:25px;\n"
                                     "")
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

        # Action Button Handle
        self.btnBack.clicked.connect(self.backMenu)
        self.btnExport.clicked.connect(self.exportAction)

    def retranslateUi(self, ExportMenu):
        _translate = QtCore.QCoreApplication.translate
        ExportMenu.setWindowTitle(_translate("ExportMenu", "SIMAKET"))
        self.lblSubsribe.setText(_translate(
            "ExportMenu", self.getActivate()))
        self.btnBack.setText(_translate("ExportMenu", "back to menu"))
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
            lin = QtWidgets.QMessageBox(self.centralwidget)
            lin.setText('Complete the form')
            lin.exec()
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
                    lin = QtWidgets.QMessageBox(self.centralwidget)
                    lin.setText('Done')
                    lin.exec()

                f += 1

    def backMenu(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExportMenu = QtWidgets.QMainWindow()
    ui = Ui_ExportMenu()
    ui.setupUi(ExportMenu)
    ExportMenu.show()
    sys.exit(app.exec_())

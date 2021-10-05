# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from models.activateHelper import activateHelper
from models.databaseLite import databaseLite


class Ui_ViewMenu(object):
    def setupUi(self, ViewMenu):
        ViewMenu.setObjectName("ViewMenu")
        ViewMenu.resize(800, 600)
        ViewMenu.setMinimumSize(QtCore.QSize(800, 600))
        ViewMenu.setMaximumSize(QtCore.QSize(800, 600))
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
        self.label.setStyleSheet("background-color: rgb(0, 173, 239);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:1px solid white;")
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
        self.btnBack.setText(_translate("ViewMenu", "back to menu"))
        item = self.tableView.horizontalHeaderItem(0)
        item.setText(_translate("ViewMenu", "Commerce"))
        item = self.tableView.horizontalHeaderItem(1)
        item.setText(_translate("ViewMenu", "Tanggal"))
        item = self.tableView.horizontalHeaderItem(2)
        item.setText(_translate("ViewMenu", "Jumlah"))
        self.btnRefresh.setText(_translate("ViewMenu", "Refresh"))
        self.btnDelete.setText(_translate("ViewMenu", "Delete All Data"))

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

    def loadAllData(self):

        dblite = databaseLite()
        cts = dblite.get_count("tb_scrap", "id_scrap", "")
        self.tableView.setRowCount(cts)
        tbrow = 0
        rowalls = dblite.read_dateabase("tb_detail", "tb_commerce.name_commerce as commerce,tb_scrap.tgl_scrap as dates ,COUNT(tb_detail.id_detail) as counts",
                                        "INNER JOIN tb_scrap ON tb_scrap.id_scrap = tb_detail.id_scrape INNER JOIN tb_commerce ON tb_commerce.id_commerce = tb_scrap.id_commerce", "", "tb_detail.id_scrape", "tgl_scrap DESC", "50")
        for row in rowalls:
            self.tableView.setItem(
                tbrow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableView.setItem(
                tbrow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableView.setItem(
                tbrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))

            tbrow += 1

    def deleteAllData(self):
        linz = QtWidgets.QMessageBox.question(self.centralwidget, "Confirm Delete", "Are you sure to delete all data?",
                                              QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No)
        if linz == QtWidgets.QMessageBox.StandardButton.Yes:
            dblite = databaseLite()
            dblite.truncate_database()

        lin = QtWidgets.QMessageBox(self.centralwidget)
        lin.setText("Delete All Data Done")
        lin.exec()
        self.loadAllData()

    def backMenu(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewMenu = QtWidgets.QMainWindow()
    ui = Ui_ViewMenu()
    ui.setupUi(ViewMenu)
    ViewMenu.show()
    sys.exit(app.exec_())

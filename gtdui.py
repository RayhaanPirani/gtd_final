# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gtd.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import gtdbasic_ui as basic
import gtdmodel_ui as model
import gtdanalyze_ui as analyze
import os, pathlib, qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebKitWidgets

class Ui_MainWindow(object):
    con = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 570, 1341, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 371, 215))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 351, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 60, 351, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 90, 351, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 120, 351, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 150, 351, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 180, 181, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 180, 171, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 10, 965, 551))
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget = QtWebKitWidgets.QWebView(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(10, 30, 945, 521))
        self.widget.setObjectName("widget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 371, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 271, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 550, 46, 13))
        self.label.setObjectName("label")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 300, 71, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.pushButton_9.raise_()

        self.pushButton.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.load_db)
        self.pushButton.clicked.connect(self.list_with_most_attacks)
        self.pushButton_3.clicked.connect(self.visualize_with_most_attacks)
        self.pushButton_4.clicked.connect(self.list_with_most_casualties)
        self.pushButton_5.clicked.connect(self.list_by_dates)
        self.pushButton_6.clicked.connect(self.visualize_by_dates)
        self.pushButton_7.clicked.connect(self.visualize_word_cloud)
        self.pushButton_8.clicked.connect(self.visualize_world_map)
        self.pushButton_9.clicked.connect(self.close_app)

    def load_db(self):
        dbname = self.lineEdit.text()
        if dbname.endswith('_modelled.sqlite'):
            import sqlite3
            self.textBrowser.setText(self.textBrowser.toPlainText() + "\n" + "Initializing database...")
            self.con = sqlite3.connect(dbname)
            self.textBrowser.setText(self.textBrowser.toPlainText() + "\n" + "Initialization complete.")
            if self.con is not None:
                self.pushButton.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
        elif dbname.endswith('.sqlite'):
            dbname = model.normalize(self, dbname)
            import sqlite3
            self.textBrowser.setText(self.textBrowser.toPlainText() + "\n" + "Initializing database...")
            self.con = sqlite3.connect(dbname)
            self.textBrowser.setText(self.textBrowser.toPlainText() + "\n" + "Initialization complete.")
            if self.con is not None:
                self.pushButton.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
        elif dbname.endswith('.xlsx'):
            dbname = basic.start_csv_conversion(self, dbname)
            dbname = model.normalize(self, dbname)
            import sqlite3
            self.textBrowser.setText(self.textBrowser.toPlainText() + "\n" + "Initializing database...")
            self.con = sqlite3.connect(dbname)
            self.textBrowser.setText(self.textBrowser.toPlainText() + "\n" + "Initialization complete.")
            if self.con is not None:
                self.pushButton.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
        else:
            QtWidgets.QMessageBox.critical(self.pushButton_2, "Error", "Wrong input file.")

    def visualize_file(self, myfile):
        dirname = pathlib.Path(os.getcwd()).as_uri()
        self.widget.load(QtCore.QUrl(dirname + "/" + myfile))
        self.widget.show()

    def list_with_most_attacks(self):
        n, ok = QtWidgets.QInputDialog.getText(None,"GTD Analysis","Enter the maximum number to display:")
        if ok:
            analyze.attacks_by_count(self, self.con, n)

    def visualize_with_most_attacks(self):
        n, ok = QtWidgets.QInputDialog.getText(None,"GTD Analysis","Enter the maximum number to display:")
        if ok:
            analyze.attacks_by_count(self, self.con, n, visualize=True)
            self.visualize_word_cloud()

    def list_with_most_casualties(self):
        n, ok = QtWidgets.QInputDialog.getText(None,"GTD Analysis","Enter the maximum number to display:")
        if ok:
            analyze.attacks_by_casualties(self, self.con, n)

    def list_by_dates(self):
        start, ok = QtWidgets.QInputDialog.getText(None,"GTD Analysis","Enter initial date in YYYY-MM-DD format:")
        if ok:
            end, ok = QtWidgets.QInputDialog.getText(None,"GTD Analysis","Enter final date in YYYY-MM-DD format:")
            if ok:
                analyze.attacks_by_dates(self, self.con, start, end)

    def visualize_by_dates(self):
        start, ok = QtWidgets.QInputDialog.getText(None,"GTD Analysis","Enter initial date in YYYY-MM-DD format:")
        if ok:
            end, ok = QtWidgets.QInputDialog.getText(None,"GTD Analysis","Enter final date in YYYY-MM-DD format:")
            if ok:
                analyze.attacks_by_dates(self, self.con, start, end, map=True)
                self.visualize_world_map()
    
    def visualize_word_cloud(self):
        self.visualize_file('gtdcountries.htm')

    def visualize_world_map(self):
        self.visualize_file('map.html')

    def close_app(self):
        sys.exit(app.exec_())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GTD Analysis"))
        self.groupBox.setTitle(_translate("MainWindow", "Actions"))
        self.pushButton.setText(_translate("MainWindow", "List the countries with the most terror attacks"))
        self.pushButton_3.setText(_translate("MainWindow", "Visualize the countries with the most terror attacks"))
        self.pushButton_4.setText(_translate("MainWindow", "List the countries with the highest casualties"))
        self.pushButton_5.setText(_translate("MainWindow", "List countries with events between specified dates"))
        self.pushButton_6.setText(_translate("MainWindow", "Locate countries with events between specified dates"))
        self.pushButton_8.setText(_translate("MainWindow", "Show world map"))
        self.pushButton_7.setText(_translate("MainWindow", "Show word cloud"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Visualization"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Load file"))
        self.pushButton_2.setText(_translate("MainWindow", "Load file"))
        self.label.setText(_translate("MainWindow", "Status"))
        self.pushButton_9.setText(_translate("MainWindow", "Close app"))

if __name__ == "__main__":
    import ctypes
    myappid = u'rayhaan.gtd.v1.00'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app_icon = QtGui.QIcon()
    app_icon.addFile('icon-16.png', QtCore.QSize(16,16))
    app_icon.addFile('icon-24.png', QtCore.QSize(24,24))
    app_icon.addFile('icon-32.png', QtCore.QSize(32,32))
    app_icon.addFile('icon-48.png', QtCore.QSize(48,48))
    app_icon.addFile('icon-256.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
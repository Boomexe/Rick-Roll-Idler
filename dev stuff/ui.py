# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 729)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/assets/images/rick_face.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rickButton = QtWidgets.QPushButton(self.centralwidget)
        self.rickButton.setGeometry(QtCore.QRect(30, 70, 151, 201))
        self.rickButton.setText("")
        self.rickButton.setIcon(icon)
        self.rickButton.setIconSize(QtCore.QSize(200, 200))
        self.rickButton.setObjectName("rickButton")
        self.rickLabelHelper = QtWidgets.QLabel(self.centralwidget)
        self.rickLabelHelper.setGeometry(QtCore.QRect(20, 270, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.rickLabelHelper.setFont(font)
        self.rickLabelHelper.setObjectName("rickLabelHelper")
        self.rickCounter = QtWidgets.QLabel(self.centralwidget)
        self.rickCounter.setGeometry(QtCore.QRect(30, 35, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.rickCounter.setFont(font)
        self.rickCounter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rickCounter.setObjectName("rickCounter")
        self.upgradesLabel = QtWidgets.QLabel(self.centralwidget)
        self.upgradesLabel.setGeometry(QtCore.QRect(320, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.upgradesLabel.setFont(font)
        self.upgradesLabel.setObjectName("upgradesLabel")
        self.rickRollEfficiencyButton = QtWidgets.QPushButton(self.centralwidget)
        self.rickRollEfficiencyButton.setGeometry(QtCore.QRect(320, 80, 391, 28))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.rickRollEfficiencyButton.setFont(font)
        self.rickRollEfficiencyButton.setObjectName("rickRollEfficiencyButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuGame = QtWidgets.QAction(MainWindow)
        self.menuGame.setWhatsThis("")
        self.menuGame.setObjectName("menuGame")
        self.menuSettings = QtWidgets.QAction(MainWindow)
        self.menuSettings.setObjectName("menuSettings")
        self.menuStatistics = QtWidgets.QAction(MainWindow)
        self.menuStatistics.setObjectName("menuStatistics")
        self.menuUpdate_Log = QtWidgets.QAction(MainWindow)
        self.menuUpdate_Log.setObjectName("menuUpdate_Log")
        self.menuMenu.addAction(self.menuGame)
        self.menuMenu.addAction(self.menuSettings)
        self.menuMenu.addAction(self.menuStatistics)
        self.menuMenu.addAction(self.menuUpdate_Log)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rickrolling"))
        self.rickLabelHelper.setText(_translate("MainWindow", "Click the Rickroll to earn"))
        self.rickCounter.setText(_translate("MainWindow", "0 Rick Rolls"))
        self.upgradesLabel.setText(_translate("MainWindow", "Upgrades"))
        self.rickRollEfficiencyButton.setText(_translate("MainWindow", "Rick Roll Efficiency (Currently Owned: 0) Price: 10 Rick Rolls"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuGame.setText(_translate("MainWindow", "Game"))
        self.menuGame.setShortcut(_translate("MainWindow", "1"))
        self.menuSettings.setText(_translate("MainWindow", "Settings"))
        self.menuSettings.setShortcut(_translate("MainWindow", "2"))
        self.menuStatistics.setText(_translate("MainWindow", "Statistics"))
        self.menuStatistics.setShortcut(_translate("MainWindow", "3"))
        self.menuUpdate_Log.setText(_translate("MainWindow", "Update Log"))
        self.menuUpdate_Log.setShortcut(_translate("MainWindow", "4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
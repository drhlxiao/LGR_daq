# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1392, 882)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(600, 300))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabControls = QtWidgets.QWidget()
        self.tabControls.setObjectName("tabControls")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabControls)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tabControls)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ipAddressInput = QtWidgets.QLineEdit(self.groupBox)
        self.ipAddressInput.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ipAddressInput.setObjectName("ipAddressInput")
        self.horizontalLayout.addWidget(self.ipAddressInput)
        self.portLabel = QtWidgets.QLabel(self.groupBox)
        self.portLabel.setObjectName("portLabel")
        self.horizontalLayout.addWidget(self.portLabel)
        self.portInput = QtWidgets.QSpinBox(self.groupBox)
        self.portInput.setMaximum(65535)
        self.portInput.setProperty("value", 1002)
        self.portInput.setObjectName("portInput")
        self.horizontalLayout.addWidget(self.portInput)
        self.connectBtn = QtWidgets.QPushButton(self.groupBox)
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout.addWidget(self.connectBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.basicOperationGroup = QtWidgets.QGroupBox(self.tabControls)
        self.basicOperationGroup.setObjectName("basicOperationGroup")
        self.verticalLayout_3.addWidget(self.basicOperationGroup)
        self.readoutsGroup = QtWidgets.QGroupBox(self.tabControls)
        self.readoutsGroup.setObjectName("readoutsGroup")
        self.verticalLayout_3.addWidget(self.readoutsGroup)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tabControls, "")
        self.tabRegisters = QtWidgets.QWidget()
        self.tabRegisters.setObjectName("tabRegisters")
        self.tabWidget.addTab(self.tabRegisters, "")
        self.tabHousekeeping = QtWidgets.QWidget()
        self.tabHousekeeping.setObjectName("tabHousekeeping")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabHousekeeping)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.hkSingleReadBtn = QtWidgets.QPushButton(self.tabHousekeeping)
        self.hkSingleReadBtn.setObjectName("hkSingleReadBtn")
        self.gridLayout_5.addWidget(self.hkSingleReadBtn, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tabHousekeeping)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 2, 1, 1)
        self.hkPeriodInput = QtWidgets.QSpinBox(self.tabHousekeeping)
        self.hkPeriodInput.setMinimumSize(QtCore.QSize(90, 0))
        self.hkPeriodInput.setProperty("value", 1)
        self.hkPeriodInput.setObjectName("hkPeriodInput")
        self.gridLayout_5.addWidget(self.hkPeriodInput, 0, 3, 1, 1)
        self.hkStartBtn = QtWidgets.QPushButton(self.tabHousekeeping)
        self.hkStartBtn.setObjectName("hkStartBtn")
        self.gridLayout_5.addWidget(self.hkStartBtn, 0, 4, 1, 1)
        self.hkTableWidget = QtWidgets.QTableWidget(self.tabHousekeeping)
        self.hkTableWidget.setObjectName("hkTableWidget")
        self.hkTableWidget.setColumnCount(4)
        self.hkTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.hkTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hkTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hkTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hkTableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout_5.addWidget(self.hkTableWidget, 1, 0, 1, 5)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.tabHousekeeping, "")
        self.tabScience = QtWidgets.QWidget()
        self.tabScience.setObjectName("tabScience")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabScience)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sciStartDRSBtn = QtWidgets.QPushButton(self.tabScience)
        self.sciStartDRSBtn.setObjectName("sciStartDRSBtn")
        self.horizontalLayout_3.addWidget(self.sciStartDRSBtn)
        self.sciStopDRSBtn = QtWidgets.QPushButton(self.tabScience)
        self.sciStopDRSBtn.setObjectName("sciStopDRSBtn")
        self.horizontalLayout_3.addWidget(self.sciStopDRSBtn)
        self.sciTrigDRSBtn = QtWidgets.QPushButton(self.tabScience)
        self.sciTrigDRSBtn.setObjectName("sciTrigDRSBtn")
        self.horizontalLayout_3.addWidget(self.sciTrigDRSBtn)
        self.sciSingReadBtn = QtWidgets.QPushButton(self.tabScience)
        self.sciSingReadBtn.setObjectName("sciSingReadBtn")
        self.horizontalLayout_3.addWidget(self.sciSingReadBtn)
        spacerItem2 = QtWidgets.QSpacerItem(368, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.tabScience)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.widget_2 = QtWidgets.QWidget(self.tabScience)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_6.addWidget(self.widget_2)
        self.tabWidget.addTab(self.tabScience, "")
        self.tabCalibration = QtWidgets.QWidget()
        self.tabCalibration.setObjectName("tabCalibration")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabCalibration)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.calStartBtn = QtWidgets.QPushButton(self.tabCalibration)
        self.calStartBtn.setObjectName("calStartBtn")
        self.horizontalLayout_4.addWidget(self.calStartBtn)
        self.calStopBtn = QtWidgets.QPushButton(self.tabCalibration)
        self.calStopBtn.setObjectName("calStopBtn")
        self.horizontalLayout_4.addWidget(self.calStopBtn)
        spacerItem3 = QtWidgets.QSpacerItem(518, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.tabCalibration)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.widget = QtWidgets.QWidget(self.tabCalibration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.widget)
        self.tabWidget.addTab(self.tabCalibration, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1392, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(600, 250))
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents_3)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_3)
        self.actionIP = QtWidgets.QAction(MainWindow)
        self.actionIP.setObjectName("actionIP")
        self.menuSettings.addAction(self.actionIP)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HIT DAQ"))
        self.groupBox.setTitle(_translate("MainWindow", "Connection"))
        self.label.setText(_translate("MainWindow", "IP"))
        self.ipAddressInput.setText(_translate("MainWindow", "10.42.0.130"))
        self.portLabel.setText(_translate("MainWindow", "Port"))
        self.connectBtn.setText(_translate("MainWindow", "Connect"))
        self.basicOperationGroup.setTitle(_translate("MainWindow", "Commands"))
        self.readoutsGroup.setTitle(_translate("MainWindow", "Readout"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabControls), _translate("MainWindow", "Configuration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRegisters), _translate("MainWindow", "Registers"))
        self.hkSingleReadBtn.setText(_translate("MainWindow", "Single-shot read"))
        self.label_2.setText(_translate("MainWindow", "Updated period (s)"))
        self.hkStartBtn.setText(_translate("MainWindow", "Start"))
        item = self.hkTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.hkTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.hkTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Raw Value"))
        item = self.hkTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Eng. Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHousekeeping), _translate("MainWindow", "Housekeeping"))
        self.sciStartDRSBtn.setText(_translate("MainWindow", "Start DRS read  "))
        self.sciStopDRSBtn.setText(_translate("MainWindow", "Stop DRS "))
        self.sciTrigDRSBtn.setText(_translate("MainWindow", "trigger DRS"))
        self.sciSingReadBtn.setText(_translate("MainWindow", "Single read per ch."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScience), _translate("MainWindow", "Science"))
        self.calStartBtn.setText(_translate("MainWindow", "Start calibration"))
        self.calStopBtn.setText(_translate("MainWindow", "Stop calibration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalibration), _translate("MainWindow", "Calibration"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings"))
        self.label_3.setText(_translate("MainWindow", "Log"))
        self.actionIP.setText(_translate("MainWindow", "IP"))
import mainwindow_rc5_rc

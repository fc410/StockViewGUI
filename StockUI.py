from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QLineEdit
from pyqtgraph import PlotWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime.now()
df = web.DataReader('AAPL', 'yahoo',start, end)
print(df.head())
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 1000, 600))
        self.graphicsView.setObjectName("graphicsView")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 615, 1000, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.qLineEdit = QtWidgets.QLineEdit(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.qLineEdit.setObjectName("lineEdit")

        self.pushButton_7 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("searchButton")

        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_3 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_4 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_5 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_6 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda:self.one_day_clicked())
        self.pushButton_2.clicked.connect(lambda:self.one_month_clicked())
        self.pushButton_3.clicked.connect(lambda:self.three_months_clicked())
        self.pushButton_4.clicked.connect(lambda:self.one_year_clicked())
        self.pushButton_5.clicked.connect(lambda:self.five_years_clicked())
        self.pushButton_7.clicked.connect(lambda:self.search_button_clicked())
        self.pushButton_6.clicked.connect(lambda:self.max_clicked())
        

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_7.setText(_translate("MainWindow", "Search"))
        self.pushButton.setText(_translate("MainWindow", "1 day"))
        self.pushButton_2.setText(_translate("MainWindow", "1 Month"))
        self.pushButton_3.setText(_translate("MainWindow", "3 Months"))
        self.pushButton_4.setText(_translate("MainWindow", "1 Year"))
        self.pushButton_5.setText(_translate("MainWindow", "5 Years"))
        self.pushButton_6.setText(_translate("MainWindow", "Max"))

    def search_button_clicked(self):
        self.graphicsView.clear()
        start = datetime.datetime(2020, 4, 8)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'])

    def one_day_clicked(self):
        self.graphicsView.clear()
        start = datetime.datetime(2020,4,8)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'])
    
    def one_month_clicked(self):
        self.graphicsView.clear()
        start = datetime.datetime(2020,3,8)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'])

    def three_months_clicked(self):
        self.graphicsView.clear()
        start = datetime.datetime(2020,1,8)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'])

    def one_year_clicked(self):
        self.graphicsView.clear()
        start = datetime.datetime(2019,1,1)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'])
    
    def five_years_clicked(self):
        self.graphicsView.clear()
        start = datetime.datetime(2015, 1, 1)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'])

    def max_clicked(self):
        self.graphicsView.clear()
        start = datetime.datetime(2000, 1, 1)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'])

    def clear(self):
        self.graphicsView.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
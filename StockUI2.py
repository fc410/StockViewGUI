from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtChart import QCandlestickSeries
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QLineEdit, QCheckBox, QLabel
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
#import mplfinance
#from mpl_finance import candlestick_ohlc




# df['SMA_0.25'] = df.iloc[:,1].rolling(window=0.25).mean()
pen = pg.mkPen(color=(0, 0, 0))

class Ui_MainWindow(object):
    start = ('2021-01-01')
    end = datetime.datetime.now()
    df = web.DataReader('AAPL', 'yahoo', start=start, end=end)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 595, 500, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.qLineEdit = QtWidgets.QLineEdit(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.qLineEdit.setObjectName("lineEdit")

        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 1000, 550))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground('w')
        self.graphicsView.setLabel('left', "<span style=\"color:black;font-size:30px\">Dollars</span>")
        self.graphicsView.setLabel('bottom', "<span style=\"color:black;font-size:30px\">Date</span>")
        

        self.split = QtWidgets.QSplitter(self.centralwidget)
        self.split.setGeometry(QtCore.QRect(10, 695, 800, 41))
        self.split.setOrientation(QtCore.Qt.Horizontal)
        self.split.setObjectName("splitter2")

        self.split2 = QtWidgets.QSplitter(self.centralwidget)
        self.split2.setGeometry(QtCore.QRect(10, 645, 800, 41))
        self.split2.setOrientation(QtCore.Qt.Horizontal)
        self.split2.setObjectName("splitter3")

        self.series = QCandlestickSeries()
        self.series.setDecreasingColor(Qt.red)
        self.series.setIncreasingColor(Qt.green)

        self.searchButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")

        self.fiveDayMA = QtWidgets.QCheckBox(self.split)
        self.fiveDayMA.setFont(font)
        self.fiveDayMA.setObjectName("fiveDayMA")
        
        self.tenDayMA = QtWidgets.QCheckBox(self.split)
        self.tenDayMA.setFont(font)
        self.tenDayMA.setObjectName("oneMonthMA")

        self.twentyDayMA = QtWidgets.QCheckBox(self.split)
        self.twentyDayMA.setFont(font)
        self.twentyDayMA.setObjectName("twoMonthMA")

        self.oneMonthMA = QtWidgets.QCheckBox(self.split)
        self.oneMonthMA.setFont(font)
        self.oneMonthMA.setObjectName("threeMonthMA")


        self.oneDayButton = QtWidgets.QPushButton(self.split2)
        self.oneDayButton.setFont(font)
        self.oneDayButton.setObjectName("oneDayButton")

        self.oneMonthButton = QtWidgets.QPushButton(self.split2)
        self.oneMonthButton.setFont(font)
        self.oneMonthButton.setObjectName("oneMonthButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.threeMonthButton = QtWidgets.QPushButton(self.split2)
        self.threeMonthButton.setFont(font)
        self.threeMonthButton.setObjectName("threeMonthButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.oneYearButton = QtWidgets.QPushButton(self.split2)
        self.oneYearButton.setFont(font)
        self.oneYearButton.setObjectName("oneYearButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.fiveYearButton = QtWidgets.QPushButton(self.split2)
        self.fiveYearButton.setFont(font)
        self.fiveYearButton.setObjectName("fiveYearButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.maxButton = QtWidgets.QPushButton(self.split2)
        self.maxButton.setFont(font)
        self.maxButton.setObjectName("maxButton")
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

        self.oneDayButton.clicked.connect(lambda:self.one_day_clicked())
        self.oneMonthButton.clicked.connect(lambda:self.one_month_clicked())
        self.threeMonthButton.clicked.connect(lambda:self.three_months_clicked())
        self.oneYearButton.clicked.connect(lambda:self.one_year_clicked())
        self.fiveYearButton.clicked.connect(lambda:self.five_years_clicked())
        self.searchButton.clicked.connect(lambda:self.search_button_clicked())
        self.maxButton.clicked.connect(lambda:self.max_clicked())
        self.fiveDayMA.clicked.connect(lambda:self.five_day_ma_clicked(self.fiveDayMA.isChecked()))
        self.tenDayMA.clicked.connect(lambda:self.ten_day_ma_clicked(self.tenDayMA.isChecked()))
        self.twentyDayMA.clicked.connect(lambda:self.twenty_day_ma_clicked(self.twentyDayMA.isChecked()))
        self.oneMonthMA.clicked.connect(lambda:self.one_month_ma_clicked(self.oneMonthMA.isChecked()))
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.oneDayButton.setText(_translate("MainWindow", "1 day"))
        self.oneMonthButton.setText(_translate("MainWindow", "1 Month"))
        self.threeMonthButton.setText(_translate("MainWindow", "3 Months"))
        self.oneYearButton.setText(_translate("MainWindow", "1 Year"))
        self.fiveYearButton.setText(_translate("MainWindow", "5 Years"))
        self.maxButton.setText(_translate("MainWindow", "Max"))
        self.fiveDayMA.setText(_translate("MainWindow", "5 Days MA"))
        self.tenDayMA.setText(_translate("MainWindow", "10 Days MA"))
        self.twentyDayMA.setText(_translate("MainWindow", "20 days MA"))
        self.oneMonthMA.setText(_translate("MainWindow", "1 Month MA"))

    def search_button_clicked(self):
        self.graphicsView.clear()
        self.start = datetime.datetime(2020,5, 11)
        self.end = datetime.datetime.now()
        self.df = web.DataReader(self.qLineEdit.text(), 'yahoo', self.start, self.end)
        stock = self.qLineEdit.text()
        stock = stock.upper() + " Stock"
        self.graphicsView.plot(self.df['Adj Close'], label='AAPL', pen=pen)
        self.graphicsView.setTitle(stock)

    def one_day_clicked(self):
        self.graphicsView.clear()
        global start, end, df
        start = datetime.datetime(2020,5,11)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        stock = self.qLineEdit.text()
        stock = stock.upper() + " Stock"
        self.graphicsView.plot(df['Adj Close'], pen=pen)
    
    def one_month_clicked(self):
        self.graphicsView.clear()
        global start, end, df
        start = datetime.datetime(2020,4,1)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'], pen=pen)

    def three_months_clicked(self):
        self.graphicsView.clear()
        global start, end, df
        start = datetime.datetime(2020,2,1)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'], pen=pen)

    def one_year_clicked(self):
        self.graphicsView.clear()
        global start, end, df
        start = datetime.datetime(2019,1,1)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'], pen=pen)
    
    def five_years_clicked(self):
        self.graphicsView.clear()
        global start, end, df
        start = datetime.datetime(2015, 1, 1)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'], pen=pen)

    def max_clicked(self):
        self.graphicsView.clear()
        global start, end, df
        start = datetime.datetime(1990, 1, 1)
        end = datetime.datetime.now()
        df = web.DataReader(self.qLineEdit.text(), 'yahoo', start, end)
        self.graphicsView.plot(df['Adj Close'], pen=pen)
    
    def five_day_ma_clicked(self, chx):
        pen2 = pg.mkPen(color=(255, 0, 0))
        if chx:
            #self.graphicsView.clear()
            df['SMA_5'] = df.iloc[:,1].rolling(window=5).mean()
            df.fillna(0, inplace=True)
            self.graphicsView.plot(df['Adj Close'], pen=pen)
            self.graphicsView.plot(df['SMA_5'],label="5 Day MA", pen=pen2)
        else:
            self.graphicsView.clear()
            #if self.tenDayMA.isChecked():
            #    self.graphicsView.plot(df['SMA_10'])
            #elif self.twentyDayMA.isChecked():
            #    self.graphicsView.plot(df['SMA_20'])
            #elif self.oneMonthMA.isChecked():
            #    self.graphicsView.plot(df['SMA_30'])
            self.graphicsView.plot(df['Adj Close'], pen=pen)

    def check(self):
        if self.tenDayMA.isChecked() and self.twentyDayMA.isChecked() and self.fiveDayMA.ischecked() and self.oneMonthMA.isChecked():
            self.graphicsView.plot(df['SMA_5'])
            self.graphicsView.plot(df['SMA_10'])
            self.graphicsView.plot(df['SMA_20'])
            self.graphicsView.plot(df['SMA_30'])
        if self.tenDayMA.isChecked() and self.twentyDayMA.isChecked() and self.oneMonthMA.isChecked():
            self.graphicsView.plot(df['SMA_10'])
            self.graphicsView.plot(df['SMA_20'])
            self.graphicsView.plot(df['SMA_30'])
    
    def ten_day_ma_clicked(self,chx):
        pen3 = pg.mkPen(color=(0, 0, 255))
        if chx:
            #self.graphicsView.clear()
            df['SMA_10'] = df.iloc[:,1].rolling(window=10).mean()
            df.fillna(0, inplace=True)
            self.graphicsView.plot(df['Adj Close'], pen=pen)
            self.graphicsView.plot(df['SMA_10'],label="10 Day MA", pen=pen3)
        else:
            self.graphicsView.clear()
            self.graphicsView.plot(df['Adj Close'], pen=pen)

    def twenty_day_ma_clicked(self, chx):
        pen4 = pg.mkPen(color=(0, 128, 0))
        if chx:
            #self.graphicsView.clear()
            df['SMA_15'] = df.iloc[:,1].rolling(window=15).mean()
            df.fillna(0, inplace=True)
            self.graphicsView.plot(df['Adj Close'], pen=pen)
            self.graphicsView.plot(df['SMA_15'], pen=pen4)
        else:
            self.graphicsView.clear()
            self.graphicsView.plot(df['Adj Close'], pen=pen)
    
    def one_month_ma_clicked(self, chx):
        pen5 = pg.mkPen(color=(255, 165, 0))
        if chx:
            #self.graphicsView.clear()
            df['SMA_20'] = df.iloc[:,1].rolling(window=20).mean()
            df.fillna(0, inplace=True)
            print(df.head(40))
            self.graphicsView.plot(df['Adj Close'], pen=pen)
            self.graphicsView.plot(df['SMA_20'],label="3 Month MA", pen=pen5)
        else:
            self.graphicsView.clear()
            self.graphicsView.plot(df['Adj Close'], pen=pen)


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
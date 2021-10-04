import pandas_datareader.data as web
import datetime as dt
import sys
import matplotlib
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from dateutil.relativedelta import relativedelta

matplotlib.use('Qt5Agg')

tickers = 'AAPL'
dataframe = web.DataReader('SPY', 'yahoo', start='2019-09-10', end=dt.datetime.now())


# create a class that extends from the FigureCanvasQTAgg class
class MplCanvas(FigureCanvasQTAgg):
    """
    This class will take care of the Figure for creating a plot to add graphing
    and plotting in PyQt
    """

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # Create a Figure instance to draw plots on
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # add a subplot
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

        # Set the label for the x-axis as Date in (YYYY-MM)
        self.axes.set_xlabel('Date in (YYYY-MM)')
        # Set the label for the y-axis as Amount in ($)
        self.axes.set_ylabel('Amount in ($)')


class MainWindow(QtWidgets.QMainWindow):
    END = dt.date.today()
    start = '2021-01-01'
    dataframe = web.DataReader('AAPL', 'yahoo', start=start, end=END)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.sc = MplCanvas(self, width=8, height=7, dpi=100)
        # set self.sc as the central widget
        self.setCentralWidget(self.sc)
        self.sc.axes.set_title('Type a companys ticker symbol')
        # Set the window title to Stock Graphs
        self.setWindowTitle('Stock Graphs')

        # Creating a search text box
        # create a QlineEdit from PyQt5 Widgets
        self.search_text = QtWidgets.QLineEdit(self)
        # move the QLineEdit to x, y coordinates respectively
        self.search_text.move(150, 50)

        # Creating a search button
        # Create a QPushButton from the PyQt5 QtWidgets
        self.search_button = QtWidgets.QPushButton(self)
        # Set the text in the search button to "Search"
        self.search_button.setText("Search")
        # Move the search button to x, y coordinate respectively
        self.search_button.move(250, 50)
        # If the search button is clicked have the search_button_clicked button
        # function handle the event
        self.search_button.clicked.connect(self.search_button_clicked)

        # Creating a 1 day button
        # Create a QPushButton form the PyQt5 QtWidgets
        self.one_day_button = QtWidgets.QPushButton(self)
        # Set the text in the one day button to "1 day"
        self.one_day_button.setText("1 day")
        # Move the one day button to x, y respectively
        self.one_day_button.move(350, 50)
        # If the one day button is clicked then have the one_day_button_clicked
        # function handle the event
        self.one_day_button.clicked.connect(self.one_day_button_clicked)

        # Creating a 1 week button
        # Create a QPushButton from the PyQt5 QtWidgets
        self.one_week_button = QtWidgets.QPushButton(self)
        # Set the text of the one week button to "1 week"
        self.one_week_button.setText("1 week")
        # Move the one week button to x, y coordinates on the main window respectively
        self.one_week_button.move(450, 50)
        # If the one week button is clicked then have the one_week_button_clicked
        # function handle the event
        self.one_week_button.clicked.connect(self.one_week_button_clicked)

        # Creating a 2 week button
        # Create a QPushButton from the PyQt5 QtWidgets
        self.two_week_button = QtWidgets.QPushButton(self)
        # Set the text of the two week button to "2 weeks"
        self.two_week_button.setText("2 weeks")
        # Move the two week button to x, y coordinates of the main window respectively
        self.two_week_button.move(550, 50)
        # if the two week button is clicked then let the two_week_button_clicked function
        # handle the event
        self.two_week_button.clicked.connect(self.two_weeks_button_clicked)

        # Creating a 1 month button
        # Create a QPushButton from the PyQt5 QtWidgets
        self.one_month_button = QtWidgets.QPushButton(self)
        # Set the text of the one month button to "1 month"
        self.one_month_button.setText("1 month")
        # Move the one month button to x, y coordinates of the main window respectively
        self.one_month_button.move(650, 50)
        # If the one month button is clicked then have the one_month_button_clicked
        # function handle the event
        self.one_month_button.clicked.connect(self.one_month_button_clicked)

        # Creating a 3 month button
        # Create a QPushButton from the PyQt5 QtWidgets
        self.three_months_button = QtWidgets.QPushButton(self)
        # Set the text of the three month button to "3 months"
        self.three_months_button.setText("3 months")
        # Move the three month button to x,y coordinates of the main window respectively
        self.three_months_button.move(750, 50)
        # If the three month button is pressed have the three_months_button_clicked
        # function handle the event
        self.three_months_button.clicked.connect(self.three_months_button_clicked)

        # Creating a 1 year button
        # Create a QPushButton from the PyQt5 QtWidgets
        self.one_year_button = QtWidgets.QPushButton(self)
        # Set the text of the one year button to "1 year"
        self.one_year_button.setText("1 year")
        # Move the one year button to an x,y location of the main window
        self.one_year_button.move(850, 50)
        # If the one year button is clicked then the one_year_button_clicked
        # function will handle the event
        self.one_year_button.clicked.connect(self.one_year_button_clicked)

        # Creating a 5 year button
        # Create a QPushButton using the PyQt5 QtWidgets library
        self.five_years_button = QtWidgets.QPushButton(self)
        # Set the text of the 5 year button to "5 years"
        self.five_years_button.setText("5 years")
        # Move the five year button to an x,y coordinate of the main window
        self.five_years_button.move(950, 50)
        # If the five year button is clicked then the five_year_button_clicked
        # function will handle the event
        self.five_years_button.clicked.connect(self.five_years_button_clicked)

        # Creating a 20 day moving average checkmark
        # Create a QCheckBox using the PyQt5 QtWidgets library
        self.twenty_day_ma = QtWidgets.QCheckBox(self)
        # Set the text of the twenty day ma to '20 Day MA'
        self.twenty_day_ma.setText('20 Day MA')
        # Move the checkBox to an x,y coordinate of the main window
        self.twenty_day_ma.move(500, 930)
        # If the 20 day ma is checked then the twenty_ma_checked function
        # will handle the event
        self.twenty_day_ma.clicked.connect(self.twenty_ma_checked)

        # Creating a 50 day moving average checkmark
        # Create a QCheckBox using the PyQt5 QtWidgets library
        self.fifty_day_ma = QtWidgets.QCheckBox(self)
        # Set the text of the 50 day ma to '50 Day MA'
        self.fifty_day_ma.setText('50 Day MA')
        # Move the 50 day ma to an x,y coordinate of the main window
        self.fifty_day_ma.move(600, 930)
        # If the 50 day ma is checked then the fifty_ma_checked function
        # will handle the event
        self.fifty_day_ma.clicked.connect(self.fifty_ma_checked)

        # Creating a 200 day moving average checkmark
        # Create a QCheckBox using the PyQt QtWidgets library
        self.two_hundred_day_ma = QtWidgets.QCheckBox(self)
        # Set the text of the 200 day ma to '200 Day MA'
        self.two_hundred_day_ma.setText('200 Day MA')
        # Move the 200 day ma to an x,y coordiante of the main window
        self.two_hundred_day_ma.move(700, 930)
        # If the 200 day ma is checked then the two_hundred_ma_checked function
        # will handle the event
        self.two_hundred_day_ma.clicked.connect(self.two_hundred_ma_checked)

        # Set the geometry of the main window and place the main window at a specific
        # location from the users screen (userscreenX, userscreenY, mainscreenWidth, mainscreenHeight)
        self.setGeometry(375, 39, 1200, 989)

        # Update the screen
        self.show()

    def search_button_clicked(self):
        """
        This function handles the event of when the search button is clicked.
        This function first gets the ticker from the qLineEdit and uses it to
        search data from the company using the Yahoo API and padas_datareader
        and draws the adj close data on the graph
        :return: A drawn graph of the specified company the user is trying to search. The y-axis will
                 be the price of the company's stock and the x-axis will be the date.
        """
        # Stores the text of the search qLineEdit into a variable name ticker
        ticker = self.search_text.text().upper()

        # Look up the ticker data using pandas_datareader using the yahoo API
        self.dataframe = web.DataReader(ticker, 'yahoo', start=self.start, end=dt.datetime.now())

        # Clear/Remove any data from the graph
        self.sc.axes.cla()
        # Plot the tickers data, the dates on the x-axis and the adj close prices as the y-axis
        self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'], label=ticker)
        # Set the the graph title to the ticker
        self.sc.axes.set_title(ticker)
        # Display the legend
        self.sc.axes.legend()
        self.show()

    def one_day_button_clicked(self):
        """
        This function handles the event of when the one day button was clicked.
        This functions gets the stock ticker from the qLineEdit and uses the ticker
        to search data from the company using the Yahoo API and pandas_datareader
        and will draw the the adj close data on the graph where the start date was
        one day ago from the current date.
        :return: A drawn graph of the specified company the user is trying to search. The y-axis will
                 be the price of the company's stock and the x-axis will be the date where the start day
                 will be 1 day before the current date
        """
        # Declare a variable that is equal to one day
        one_day = dt.timedelta(days=1)
        # Subtract one day from the current day
        self.start = self.END - one_day

        # Save the qLineEdit text to a variable named ticker
        ticker = self.search_text.text().upper()
        # Get the ticker data from the yahoo API using pandas_datareader
        self.dataframe = web.DataReader(ticker, 'yahoo', start=self.start, end=self.END)

        # Clear/remove any plots from the main graph
        self.sc.axes.cla()
        # Plot the ticker data onto the main graph. the Adj closing price as the y-axis and the respective
        # dates on the x-axis
        self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])

    def one_week_button_clicked(self):
        """
        This function handles the event of when the one week button was clicked.
        This functions gets the stock ticker from the qLineEdit and uses the ticker
        to search data from the company using the Yahoo API and pandas_datareader
        and will draw the the adj close data on the graph where the start date was
        one week from the current date.
        :return: A drawn graph of the specified company the user is trying to search. The y-axis will
                 be the price of the company's stock and the x-axis will be the date where the start day
                 will be 1 week from the current date
        """
        # save 7 days date onto a variable named one_week
        one_week = dt.timedelta(days=7)
        # Subtract 7 days from the present current date
        self.start = self.END - one_week

        # Save the qLineEdit text into a variable named ticker
        ticker = self.search_text.text().upper()
        # Get the ticker's data from the yahoo API using pandas_datareader
        self.dataframe = web.DataReader(ticker, 'yahoo', start=self.start, end=self.END)
        # Clear/remove any plots from the main graph
        self.sc.axes.cla()
        # Plot the tickers data onto the main graph. The tickers Adj Close price as the y-axis
        # and the respective date on the x-axis
        self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])

    def two_weeks_button_clicked(self):
        """
        This function handles the event of when the two weeks button was clicked.
        This functions gets the stock ticker from the qLineEdit and uses the ticker
        to search data from the company using the Yahoo API and pandas_datareader
        and will draw the the adj close data on the graph where the start date is
        two weeks from the current date.
        :return: A drawn graph of the specified company the user is trying to search. The y-axis will
                 be the price of the company's stock and the x-axis will be the date where the start day
                 will be 2 weeks from the current date
        """
        # Save two weeks date onto a variable named two_weeks
        two_weeks = dt.timedelta(days=14)
        # subtract two weeks from the present current date
        self.start = self.END - two_weeks

        # Save the qLineEdit text in a variable named ticker
        ticker = self.search_text.text().upper()
        # Get the ticker's data with the Yahoo API using pandas_datareader
        self.dataframe = web.DataReader(ticker, 'yahoo', start=self.start, end=self.END)
        # Clear/remove any plots from the main graph
        self.sc.axes.cla()
        # Plot the ticker's data onto the main graph. The Adj Closing price as the y-axis and
        # the respective date on the x-axis
        self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])

    def one_month_button_clicked(self):
        """
        This function handles the event of when the one month button was clicked.
        This functions gets the stock ticker from the qLineEdit and uses the ticker
        to search data from the company using the Yahoo API and pandas_datareader
        and will draw the the adj close data on the graph where the start date is
        one month from the current date.
        :return: A drawn graph of the specified company the user is trying to search. The y-axis will
                 be the price of the company's stock and the x-axis will be the date where the start day
                 will be 1 month from the current date
        """
        # Save one month in a varible named one_month
        one_month = 1
        # Subtract one month from the present day
        self.start = self.END - relativedelta(months=one_month)

        # Save the qLineEdit text in a variable named ticker
        ticker = self.search_text.text().upper()
        # Get the ticker's data with the Yahoo API using the pandas_datareader
        self.dataframe = web.DataReader(ticker, 'yahoo', start=self.start, end=self.END)
        # Clear/remove any plots from the main graph
        self.sc.axes.cla()
        # Plot the ticker's data on the main graph. The tickers Adj Closing price as the y-axis and
        # the respective date on the x-axis
        self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])

    def three_months_button_clicked(self):
        """
        This function handles the event of when the three months button was clicked.
        This functions gets the stock ticker from the qLineEdit and uses the ticker
        to search data from the company using the Yahoo API and pandas_datareader
        and will draw the the adj close data on the graph where the start date is
        three months from the current date.
        :return: A drawn graph of the specified company the user is trying to search. The y-axis will
                 be the price of the company's stock and the x-axis will be the date where the start day
                 will be 3 months from the current date
        """
        # Save three months in a variable named three_months
        three_months = 3
        # Subtract 3 months from the present date
        self.start = self.END - relativedelta(months=three_months)

        # Save the qLineEdit text in a variable named ticker
        ticker = self.search_text.text().upper()
        # Get the ticker's date from the Yahoo API using pandas_datareader
        self.dataframe = web.DataReader(ticker, 'yahoo', start=self.start, end=self.END)
        # Clear/remove any plots from the main graph
        self.sc.axes.cla()
        # Plot the tickers date onto the main graph. The ticker's Adj closing price as the y-axis and
        # the respective date as the x-axis
        self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])

    def one_year_button_clicked(self):
        """
        This function handles the event of when the one year button was clicked.
        This functions gets the stock ticker from the qLineEdit and uses the ticker
        to search data from the company using the Yahoo API and pandas_datareader
        and will draw the the adj close data on the graph where the start date is
        one year from the current date.
        :return: A drawn graph of the specified company the user is trying to search. The y-axis will
                 be the price of the company's stock and the x-axis will be the date where the start day
                 will be 1 year from the current date
        """
        # Save one year in a variable name one_year
        one_year = 1
        # Subtract one year from the present date
        self.start = self.END - relativedelta(years=one_year)

        # Save the qLineEdit text in a variable named ticker
        ticker = self.search_text.text().upper()
        # Get the ticker's stock data from the Yahoo API using pandas_datareader
        self.dataframe = web.DataReader(ticker, 'yahoo', start=self.start, end=self.END)
        # Clear/remove any plots from the main graph
        self.sc.axes.cla()
        # Plot the ticker's data on the main graph. The ticker's Adj Closing price on the y-axis and
        # the respective date on the x-axis
        self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])

    def five_years_button_clicked(self):
        """
        This function handles the event of when the five years button was clicked.
        This functions gets the stock ticker from the qLineEdit and uses the ticker
        to search data from the company using the Yahoo API and pandas_datareader
        and will draw the the adj close data on the graph where the start date is
        five years from the current date.
        :return: A drawn graph of the specified company the user is trying to search. The y-axis will
                 be the price of the company's stock and the x-axis will be the date where the start day
                 will be 5 years from the current date
        """
        # Save five years in a variable name five_years
        five_years = 5
        # Subtract five years from the present date
        self.start = self.END - relativedelta(years=five_years)

        # Save the qLineEdit in a variable named ticker
        ticker = self.search_text.text().upper()
        # Get the ticker's stock date from the Yahoo API using pandas_datareader
        self.dataframe = web.DataReader(ticker, 'yahoo', start=self.start, end=self.END)
        # Clear/remove any plots from the main graph
        self.sc.axes.cla()
        # Plot the ticker's data onto the main graph. The ticker's Adj Closing price on the y-axis
        # and the respective date on the x-axis
        self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])

    def twenty_ma_checked(self):
        """
        This Function will handle the check and unchecking events from the twenty ma checkbox.
        If the twenty day ma is checked then draw the 20 day ma line of the company on the graph,
        if its unchecked then remove the 20 day ma line from the graph
        :return: A 20 ma line drawn on the graph if the checkbox is checked or the 20 ma line removed
                 if the checkbox is unchecked
        """
        # Check if the twenty day ma checkbox is checked
        if self.twenty_day_ma.checkState():
            # Create a 20day ma for the dataframe using the pandas rolling function
            twenty_day_ma = self.dataframe.rolling(window=20).mean()
            # Plot the 20 day ma line onto the main graph. The twenty day ma Adj Closing price on the
            # y-axis and the respective date on the x-axis and label it 20 Day MA
            self.sc.axes.plot(twenty_day_ma.index, twenty_day_ma['Adj Close'], label='20 Day MA')
            # show the legend of the plots
            self.sc.axes.legend()
        # Check if the twenty day ma checkbox is unchecked
        if not self.twenty_day_ma.checkState():
            # Clear or remove all plots from the main graph
            self.sc.axes.cla()

            self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])

    def fifty_ma_checked(self):
        """
        This Function will handle the check and unchecking events from the fifty ma checkbox.
        If the fifty day ma is checked then draw the 50 day ma line of the company on the graph,
        if its unchecked then remove the 50 day ma line from the graph
        :return: A 50 ma line drawn on the graph if the checkbox is checked or the 50 ma line removed
                 if the checkbox is unchecked
        """
        # Check to see if the fifty day ma was checked
        if self.fifty_day_ma.checkState():
            # Create a 50 day MA for the dataframe using the pandas rolling function
            fifty_day_ma = self.dataframe.rolling(window=50).mean()
            # Plot the fifty day ma onto the main graph. The fifty day ma Adj closing price as the y-axis
            # and the respective date on the x-axis
            self.sc.axes.plot(fifty_day_ma.index, fifty_day_ma['Adj Close'], label='50 Day MA')
            # Show the graphs legend
            self.sc.axes.legend()

        # Check to see if the fifty day ma checkbox was unchecked
        if not self.fifty_day_ma.checkState():
            # Clear/remove all plots from the main graph
            self.sc.axes.cla()
            # Plot the original dataframes data. The dataframes Adj Closing price on the y-axis
            # and the respective date on the x-axis
            self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])

    def two_hundred_ma_checked(self):
        """
        This Function will handle the check and unchecking events from the two hundred ma checkbox.
        If the two hundred day ma is checked then draw the 200 day ma line of the company on the graph,
        if its unchecked then remove the 200 day ma line from the graph
        :return: A 200 ma line drawn on the graph if the checkbox is checked or the 200 ma line removed
                 if the checkbox is unchecked
        """
        # Check to see if the two hundred day ma checkbox was checked
        if self.two_hundred_day_ma.checkState():
            # Create a 200 day ma from the dataframe data using the pandas rolling function
            two_hundred_day_ma = self.dataframe.rolling(window=200).mean()
            # Plot the 200 day ma line onto the main graph. The two hundred day ma Adj Closing price as the
            # y-axis and the respective date on the x-axis
            self.sc.axes.plot(two_hundred_day_ma.index, two_hundred_day_ma['Adj Close'], label='200 Day MA')
            # Show the plots legend
            self.sc.axes.legend()
        # Check to see if the two hundred day ma checkbox was unchecked
        if not self.two_hundred_day_ma.checkState():
            # Clear/remove all plots from the main graph
            self.sc.axes.cla()
            # Plot the original dataframe data. The dataframe's Adj Closing price as the y-axis
            # and the respective date on the x-axis
            self.sc.axes.plot(self.dataframe.index, self.dataframe['Adj Close'])


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
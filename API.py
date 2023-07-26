"""=======================================================================
 * API Class 
 * Objective: Fetch the Financial data online
========================================================================"""
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


class API:
    def API(self):
        pass
    def monthly_returns(self, ticker):
        """
        returns the monthly returns in pandas dataframe through the yfinance library

        ticker: symbol that represents a etf; string
        returns: pandas dataframe
        """
        stock = yf.download(ticker, interval = "1mo", period = "1000mo") #putting 1000 months here to get all available data from etf; as like a guaratee
        stock.reset_index(inplace=True)
        return stock['Close'] #Only getting the closing price for each month



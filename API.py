"""=======================================================================
 * API Class 
 * Objective: Fetch the Financial data online
========================================================================"""
import yfinance as yf
import pandas as pd
from datetime import datetime
import numpy as np

#ibm = pdr.get_data_yahoo(symbols='IBM', start=True, end =True)

class API:

    def __init__(self, ticker: str, interval: str, period: str):
        self.ticker=ticker
        self.interval=interval
        self.period=period

        #retrieve the dataframe of the historical price using the ticker
        self.stock = yf.download(self.ticker, interval = self.interval, period = self.period)
        self.max_stock = yf.download(self.ticker, interval = self.interval, period = "max")
        """
        putting 1000 months here to get all available data from etf; as like a guaratee
        #self.stock = yf.download("VTI", interval = "1mo", period = "1000mo") 
        """
        
    def closing_price(self):
        """
        returns the monthly returns in pandas dataframe through the yfinance library
        NOTE: the value returned behaves extremely similar to a list

        returns: pandas dataframe
        """

        self.stock.reset_index(inplace=True)

        return self.stock['Close'][:-1] #Only getting the closing price for each month

    def historical_closing_price(self):
        """
        returns historical monthly closing price
        NOTE: the value returned behaves extremely similar to a list
        
        returns: pandas dataframe
        """

        self.max_stock.reset_index(inplace=True)
        return self.max_stock['Close'][:-1]

    def compound_return(self, number_of_data: int):
        """
        returns the historical compound return
        
        returns: list
        """

        historical_price=self.historical_closing_price()
        growth_rate=[]
        inception_price=historical_price[0]

        #minus the length of compare_price because we cannot assume we know the future price at the point we start investing
        for index in range(1, len(historical_price)-len(number_of_data)):
            
            growth_rate.append((historical_price[index]/inception_price)**(12/index)-1)
            
        return growth_rate
        
    
    def standard_deviation(self, number_of_data: int):
        """
        returns standard deviation
        
        returns: float
        """
        return np.std(self.compound_return(number_of_data))
    
    def mean(self, number_of_data: int):
        """
        returns mean
        
        returns: float
        """
        return np.mean(self.compound_return(number_of_data))
    
    def z_score(self, value_compared: float):
        """
        returns z-score
        
        returns: float
        """
        return  (value_compared - self.mean()) / self.standard_deviation()
    

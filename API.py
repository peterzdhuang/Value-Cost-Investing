"""=======================================================================
 * API Class 
 * Objective: Fetch the Financial data online
 *IMPORTANT NOTE: the variable number_of_data represent the number that we must 
                  exclude from the historical data bc we cannot assume we know the future
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
        stock_tmp = yf.download(self.ticker, interval = self.interval, period = self.period)
        stock_tmp.reset_index(inplace=True)
        self.stock=stock_tmp['Close'][:-1] #Only getting the closing price for each month

        #retrieves all of the monthly returns for a ticker
        max_stock_tmp = yf.download(self.ticker, interval = self.interval, period = "max")
        max_stock_tmp.reset_index(inplace=True)
        self.max_stock=max_stock_tmp['Close'][:-1]
        
    def closing_price(self):
        """
        returns the monthly returns in pandas dataframe through the yfinance library
        NOTE: the value returned behaves extremely similar to a list

        returns: pandas dataframe
        """
        return self.stock

    def historical_closing_price(self):
        """
        returns historical monthly closing price
        NOTE: the value returned behaves extremely similar to a list
        
        returns: pandas dataframe
        """

        return self.max_stock

    def compound_return(self, number_of_data: int): 
        """
        returns the historical compound return
        
        returns: list
        """
        
        historical_price=self.max_stock
        growth_rate=[]
        inception_price=historical_price[0] #WALTER shouldnt you compare prices from month to month, not compare it with the initial price. ex. u compare the percentage change from nov to dec not percentage change from nov to jan
        
        #minus the length of compare_price because we cannot assume we know the future price at the point we start investing
        for index in range(1, (len(historical_price)-number_of_data)):
            
            #growth_rate.append((historical_price[index]/inception_price)**(12/index)-1)
            growth_rate.append((historical_price[index]-inception_price)/inception_price/(index/12))

        return growth_rate
    
    
        
    #not used
    def standard_deviation(self, number_of_data: int):
        """
        returns standard deviation
        
        returns: float
        """
        return np.std(self.compound_return(number_of_data))
    
    #not used
    def mean(self, number_of_data: int):
        """
        returns mean
        
        returns: float
        """
        return np.mean(self.compound_return(number_of_data))
    
    #not used
    def z_score(self, value_compared: float):
        """
        returns z-score
        
        returns: float
        """
        return  (value_compared - self.mean()) / self.standard_deviation()
    
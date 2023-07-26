"""=======================================================================
 * API Class 
 * Objective: Fetch the Financial data online
========================================================================"""
import yfinance as yf

class API:

    def __init__(self, tkr: str, intvl: str, prd: str):
        self.tkr=tkr
        self.intvl=intvl
        self.prd=prd

        #retrieve the dataframe of the historical price using the ticker
        self.stock = yf.download(self.tkr, interval = self.intvl, period = self.prd)
        
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

        return self.stock['Close'] #Only getting the closing price for each month
    

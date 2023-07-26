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

        #self.stock = yf.download("vti", interval = "1mo", period = "12mo")

        #retrieve the dataframe of the historical price using the ticker
        self.stock = yf.download(self.tkr, interval = self.intvl, period = self.prd)

    #return the the closing price as a list of floats
    def closing_price(self):
        tmp_dict = self.stock.to_dict()
        return list(tmp_dict["Close"].value())
    


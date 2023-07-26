"""=======================================================================
 * API Class 
 * Objective: Calculate the gain for the Lump Sum model
========================================================================"""
from API import API
class LumpSum:
    def __init__(self, amount: float, tkr: str, intvl: str, prd: str):
        self.amount=amount
        self.tkr=tkr
        self.intvl = intvl
        self.prd=prd

    #return the profit and annual growth rate of the investment as a list
    def growth_rate(self):
        price_list=API(self.tkr, self.intvl, self.prd).closing_price()
        buying_price=price_list[0]
        selling_price=price_list[len(price_list)-1]
        
        shares=self.amount/buying_price
        profit=(selling_price-buying_price)*shares

        growth_rate=((selling_price-buying_price)/buying_price)/len(price_list)*12

        return [profit, growth_rate]



"""=======================================================================
 * Value Averaging WITH Sell Class
 * Objective: Calculate the gain for Value Averaging model WIHT SELLING
========================================================================"""
from API import API

class ValueAveragingWithSell:
    def __init__(self, amount: float, ticker: str, interval: str, period: str):
        self.amount=amount #Amount of money for each month to invest
        self.api=API(ticker, interval, period)
        self.closing_price=self.api.closing_price()
    
    def get_retrun_rate(self, number_of_data: int):
        return self.api.compound_rate(number_of_data)

    def get_std(self, number_of_data: int):
        return self.api.standard_deviation(self.get_return_rate(number_of_data))

    def get_mean(self, number_of_data: int):
        return self.api.mean(self.get_return_rate(number_of_data))
    
    def get_z_score(value_compared, mean: float, std: float):
        return  (value_compared - mean) / std
    
    def decision(self):
        number_of_data=len(self.closing_price)
       
        while number_of_data>0:

            std=self.get_std(number_of_data)
            mean=self.get_mean(number_of_data)
            z_score=self.get_z_score(mean, std)
            if z_score<0:
                pass
            elif z_score>0:
                pass
            else:
                pass
            number_of_data-=1
        
        pass
    def sell(self):
        pass
    def buy(self):
        pass
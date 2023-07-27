"""=======================================================================
 * Value Averaging WITH Sell Class
 * Objective: Calculate the gain for Value Averaging model WIHT SELLING
========================================================================"""
from API import API

class ValueAveragingWithSell:
    def __init__(self, amount: float, ticker: str, interval: str, period: str):
        self.amout=amount #Amount of money for each month to invest
        self.api=API(ticker, interval, period)
        
        self.api=API(ticker, interval, period)
        
    
    def get_retrun_rate(self, number_of_data: int):
        return self.api.compound_rate(number_of_data)

    def get_std(self, number_of_data: int):
        return self.api.standard_deviation(self.get_return_rate(number_of_data))

    def get_mean(self, number_of_data: int):
        return self.api.mean(self.get_return_rate(number_of_data))
    
    def get_z_score(value_compared, mean: float, std: float):
        return  (value_compared - float) / std
    
    def decision(self):

        pass
    def sell(self):
        pass
    def buy(self):
        pass
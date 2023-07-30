"""=======================================================================
 * Value Averaging WIHTOUT SELLING class
 * Objective: Calculate the gain for the Value Averaging Model WIHTOUT SELIING
========================================================================"""


from API import API
import numpy as np
class ValueAvergingWithoutSell:
    def __init__(self, amount: int, ticker: str, interval: str, period: int):
        self.amount = amount
        self.ticker = ticker
        self.interval = interval 
        self.period = period
        self.monthly_prices = API(self.ticker, self.interval, self.period).historical_closing_price()
        self.return_rate = self.get_return_rate()
        self.length = len(self.monthly_prices) 

    def get_return_rate(self):
        change = []
        for month in range(1, len(self.monthly_prices)):
            current_month = self.monthly_prices[month] 
            last_month = self.monthly_prices[month-1]
            change.append(current_month/last_month)

        return self.outlier_discard_result(change)

    def get_std(self):
        """
        returns standard deviation
        
        returns: float
        """

        return np.std(self.return_rate)

    def get_mean(self):
        """
        returns mean
        
        returns: float
        """

        return np.mean(self.return_rate)
    
    def get_z_score(self, value_compared: float, mean: float, std: float):
        """
        returns z-score
        
        returns: float
        """
        return  (value_compared - mean) / std
    
    def outlier_discard_result(self, data_tmp):
        """
        returns a list that does not contain the outliers
        
        returns: list with float values
        """

        data=np.array(data_tmp)
        #print(data)
        Q1 = np.percentile(data, 25)
        Q3 = np.percentile(data, 75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        return data[(data >= lower_bound) & (data <= upper_bound)]
    

    def expected_returns(self):
        expected_return = []
        monthly_amount = self.amount/self.length
        
        for _ in range(self.length):
            expected_return.append(monthly_amount*self.get_mean())



        
def main():
    v = ValueAvergingWithoutSell(1000, "msft", '1mo', "max")
    
    mean = v.get_mean()
    std = v.get_std()
    z = v.get_z_score

    print(v.expected_return())
main()
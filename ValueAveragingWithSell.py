"""=======================================================================
 * Value Averaging WITH Sell Class
 * Objective: Calculate the gain for Value Averaging model WIHT SELLING
========================================================================"""
from API import API
import numpy as np

class ValueAveragingWithSell:
    def __init__(self, amount: float, ticker: str, interval: str, period: str):
        self.amount=amount #Amount of money for each month to invest
        self.total_amount=0 #Total amount of money invested in the account
        self.prior_savings=0 #Total amount of money not used to invest yet
        self.shares=0 #Amount of shares in the account after a transection

        self.monthly_investment=[] #Record of the count of shares in the account after each invesetments
        self._shares=[]

        self.api=API(ticker, interval, period)
        self.closing_price=self.api.closing_price()

        self.index=0 #For the iteration of self.closing_price
    
    def get_return_rate(self, number_of_data: int):
        """
        returns the list return_rate
        
        returns: list of float type value
        """
        
        return self.api.compound_return(number_of_data)

    def get_std(self, number_of_data: int):
        """
        returns standard deviation
        
        returns: float
        """

        return np.std(self.outlier_discard_result(self.get_return_rate(number_of_data)))

    def get_mean(self, number_of_data: int):
        """
        returns mean
        
        returns: float
        """

        return np.mean(self.outlier_discard_result(self.get_return_rate(number_of_data)))
    
    def get_z_score(self, value_compared: float, mean: float, std: float):
        """
        returns z-score
        
        returns: float
        """

        return  (value_compared - mean) / std

    def outcome(self):
        """
        returns a profot and growth rate
        
        returns: list with float type values
        """

        number_of_data=len(self.closing_price)
        
        #print(self.get_return_rate(number_of_data)) 
        
        while number_of_data>1:
            
            std=self.get_std(number_of_data)
           
            mean=self.get_mean(number_of_data)
            z_score=-0.3
            #z_score=self.get_z_score(self.get_return_rate(number_of_data)[-1], mean, std)
            #print(z_score, 'z-score')
            #print(mean, "mean")
            #print(std, "standard deviation")
            self.total_amount+=self.amount

            if z_score<0:

                if z_score<-1:
                    
                    self.buy(self, self.amount+self.prior_savings)
                    self.prior_savings=0
                    
                else:
                    #SHOULD CHANGE
                    self.prior_savings+=self.amount*0.1
                    
                    self.buy(self.amount*0.9)

                pass
            elif z_score>0:
                
                if z_score>1:

                    self.sell(self.shares)
                else:
                    #SHOULD CHANGE
                    self.shares*=0.1
                    
                    self.sell(int(self.shares*0.9))

            else:

                #SHOULD MAYBE CHANGE
                self.prior_savings+=self.amount
            
            self.index+=1
            number_of_data-=1


        selling_price=self.closing_price[len(self.closing_price)-1]
        buying_price=self.closing_price[0]
   
        profit = (self.shares*selling_price+self.prior_savings)-self.total_amount
    
        growth_rate=(selling_price/buying_price)**(12/len(self.monthly_investment))-1

        return [profit, growth_rate]
    
    def investment_record(self):
        """
        returns a list of record containing the shares in the account after each invesetments
        
        returns: list
        """
        return self.monthly_investment
        
        
    def buy(self, amount):

        self.shares+=amount/self.closing_price[self.index]
        self.monthly_investment.append(self.shares)


    def sell(self, shares):

        self.prior_savings+=shares*self.closing_price[self.index]
        
        self.shares-=shares

        self.monthly_investment.append(self.shares)

    def outlier_discard_result(self, data_tmp):
        data=np.array(data_tmp)
        #print(data)
        Q1 = np.percentile(data, 25)
        Q3 = np.percentile(data, 75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        return data[(data >= lower_bound) & (data <= upper_bound)]

    
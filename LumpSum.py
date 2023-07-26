"""=======================================================================
 * API Class 
 * Objective: Calculate the gain for the Lump Sum model
========================================================================"""


class LumpSum:
    def LumpSum(self):
        pass
    def calculate(self, lump_sum, monthly_returns):
        stocks_bought = lump_sum / monthly_returns[0]

        return monthly_returns.tail(1) * stocks_bought 
    
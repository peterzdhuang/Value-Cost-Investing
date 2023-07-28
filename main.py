"""=======================================================================
 * Main Class
 * Objective: Analyze the outcome of the three different investment strategies
 Where we test all of the code, for example the API is it's individual module. 
 Pass a ticker symbol through and it will return relevant information.
========================================================================"""
from LumpSum import LumpSum
from ValueAveragingWithSell import ValueAveragingWithSell

def main():
    LIST_OF_ETF = ["vt", "vti", "vv","ijs", "vxus", "vea", "vemax"]
    #Should be VEMAX not VEM 
    """XIU and AVDV do not have 10 years data, so excluded for now"""

    period="10y"
    interval="1mo"
    monthly_amount = 10000
    lump_sum_outcome={}
    VAwSell_outcome={}
   
    for ticker in LIST_OF_ETF:

        lump_sum=LumpSum(monthly_amount, ticker, interval, period)
        VAwSell=ValueAveragingWithSell(monthly_amount, ticker, interval, period)

        lump_sum_outcome[ticker]=lump_sum.outcome()
        VAwSell_outcome[ticker]=VAwSell.outcome()

    print("Lump Sum Result: ", lump_sum_outcome)
    print("Value Averaging with Selling Result", VAwSell_outcome)
    
    #monthly_returns = API().monthly_returns("vem")

    #print(LumpSum().calculate(LUMP_SUM, monthly_returns))

if __name__ == "__main__":
    main()

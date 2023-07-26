#Where we would test all of the code, for example the API is it's individual module. I will pass a ticker symbol through and it will return relevant information.


from API import API
from LumpSum import LumpSum

def main():
    LIST_OF_ETF = ["vt", "vti","xiu", "vv","ijs", "vxus", "vea", "avdv", "vem"]
    LUMP_SUM = 10000
    monthly_returns = API().monthly_returns("vem")

    print(LumpSum().calculate(LUMP_SUM, monthly_returns))
    
main()
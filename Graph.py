"""=======================================================================
 * Graphing Class
 * Objective: Visually shows the data through graphs
========================================================================"""
import matplotlib.pyplot as plt
from scipy.stats import norm

class NormalDistribution:
    def __init__(self, mean: float, standard_deviation: float, data_point: list, ticker: str) -> None:
        self.mean=mean
        self.standard_deviation=standard_deviation
        self.data_point=data_point
        self.ticker=ticker.upper()
      
    def graph(self):
        """
        generate the normal distribution for the data
        
        returns: None
        """

        plt.plot(self.data_point, norm.pdf(self.data_point, loc=self.mean, scale=self.standard_deviation), label='Normal Distribution')

        plt.xlabel("Growth Rate")
        plt.ylabel("Probability Density")
        plt.title(f"Normal Distribution of {self.ticker}'s growth rate")
 


class ScatterPlot:
    def __init__(self, data: list, ticker: str) -> None:
        self.data=data
        self.ticker=ticker.upper()
       
    def graph(self):
        """
        Generate the scatter plot for the data
        
        returns: None
        """

        tmp_data=[]
        tmp_set=set(self.data)
        
        for element in self.data:
            tmp_data.append(round(element, 2))
            
        tmp_set=set(tmp_data)

        adjusted_data = {key: tmp_data.count(key) for key in tmp_set}

        data_list=list(adjusted_data.keys())
        count_list=list(adjusted_data.values())

        #line plot
        plt.scatter(x=data_list, y=count_list, marker='o')

        #labels and a title
        plt.xlabel('Growth Rate')
        plt.ylabel('Count')
        plt.title(f"Scatter Plot for {self.ticker}'s Growth Rate")

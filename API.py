import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

stock = yf.download("vti", interval = "1mo", period = "12mo")
print(stock)
list = stock.values.tolist()


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.stats import norm 

# calculating VaR

def main() :
    
    df = pd.read_csv("Stock_Data/IAEX.L.csv", index_col = 'Date', parse_dates=True)
    df.drop(df.tail(1).index,inplace=True)

    calc_var(df.Close)


def calc_var(price_list) :
    
    prices = pd.Series(price_list)
    prices.dropna()

    mean = np.mean(prices)
    std_dev = np.std(prices)
    daily_returns = -prices.pct_change()

    var_90 = daily_returns.quantile(0.90)
    var_95 = daily_returns.quantile(0.95)
    var_99 = daily_returns.quantile(0.99)

    daily_returns.plot.hist(bins=30)
    plt.show()

    print("mean, stddev")
    print(mean)
    print(std_dev)

    print(f"""
    var_90 = {var_90}
    var_95 = {var_95}
    var_99 = {var_99}""")

    
     



if __name__ == "__main__" :
    main()
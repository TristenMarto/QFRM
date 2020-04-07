from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
from datetime import date, timedelta
import os
import pandas as pd 

def main():

    tickers = ['IAEX.L','VWRD.L', 'TGET.AS','EUEA.AS']

    importer(tickers, 255)
    merger(tickers)


def importer(tickers, ndays) :
    start_date = date.today() - timedelta(days=ndays)
    end_date = date.today()
    
    if not os.path.exists("Stock_Data") :
        os.makedirs("Stock_Data")
    
    for ticker in tickers :
        if not os.path.exists(f"Stock_Data/{ticker}.csv") :
            try :    
                tempdf = data.DataReader(ticker, 'yahoo', start_date, end_date)
                tempdf.to_csv(f"Stock_Data/{ticker}.csv")

            except RemoteDataError :
                print(f"no data for {ticker}")
    
        else :
            print(f"{ticker} already exists")

def merger(tickers) :
    df_combined = pd.DataFrame()

    for ticker in tickers :
        temp_df = pd.read_csv(f"Stock_Data/{ticker}.csv", index_col='Date', parse_dates=True)
        temp_df.rename(columns={"Adj Close": ticker}, inplace=True)
        temp_df.drop(columns=['High','Low','Open','Close','Volume'], axis=1, inplace=True)

        if df_combined.empty :
            df_combined = temp_df 
        else :
            df_combined = df_combined.join(temp_df, how='outer')

    print(df_combined.head())
    df_combined.to_csv("Stock_Data/combined.csv")


if __name__ == "__main__" :
    main()
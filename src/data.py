import yfinance as yf
import pandas as pd
from dataclasses import dataclass

@dataclass
class MarketData:
    price_history: pd.DataFrame
    monthly_returns:pd.DataFrame
    annual_mean_returns: pd.Series
    covariance: pd.DataFrame

class DataLoader():
    def __init__(self):
        self.data = None
    
    def fetch_data(self,tickers: str,start: str = None,end: str = None, period: str = None) -> pd.Series:
        self.data = yf.download(tickers = tickers, start=start, end=end,period=period)["Close"]
        return self.data
    
    def returns(self) -> pd.DataFrame:
        return self.data.pct_change().dropna(0)

    def monthly_returns(self) -> pd.DataFrame:
        self.returns().resample("ME").apply(lambda x: (1 + x).prod() - 1)
        return 
    
    def annual_mean_returns(self) -> pd.Series:
        return self.monthly_returns().mean() * 12
    
    def cov(self) -> pd.DataFrame:
        return self.returns
    
    def get_market_data(self) -> MarketData:
        return MarketData(
            price_history=self.fetch_data(),
            monthly_returns=self.monthly_returns(),
            annual_mean_returns=self.annual_mean_returns(),
            covariance=self.cov()
        )
        
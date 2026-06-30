from src.data import DataLoader
from src.optimisers import OptimisationEngine

def run_optimisation_engine(tickers):
    #Get the data for the tickers
    loader = DataLoader()
    loader.fetch_data(tickers, start="2020-01-01",end="2024-12-31")
    ticker_data  = loader.get_market_data()
    
    optimiser = OptimisationEngine(ticker_data.annual_mean_returns,ticker_data.covariance)
    optimiser.optimise()
    
    

if __name__ == 'main':
    tickers = ["AAPL","NVDA","MSFT","GOOGL","AMZN","META","TSLA"]
    run_optimisation_engine(tickers)
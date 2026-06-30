import numpy as np
import pandas as pd
from scipy.optimize import minimize
from dataclasses import dataclass

@dataclass
class Constraints:
    long_only: bool = True
    max_weight: float = 1.0 
    min_weight: float = 0.0

class OptimisationEngine:
    def __init__(self,annual_mean_returns,covariance, constraints: Constraints):
        self.annual_mean_returns = annual_mean_returns
        self.covariance = covariance
        
        self.constraints = constraints
        
    
    def minimise_volatility(self):
        ...
        
    def maximise_sharpe(self):
        ...
        
    def optimise():
        ...
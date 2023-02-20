from dataclasses import dataclass
import numpy as np

@dataclass()
class UserProfile:
    goal_amount: int
    target_year: int
    current_balance: int
    max_annual_amount: int
    inflation_adjust : bool
    inflation_factor: float
    portfolio_return: float
    portfolio_stdv: float

def create_one_hot(n: int):
    """ return one hot vectors"""
    a = np.arange(n + 2)
    one_h = np.zeros([n+2, n+2])
    one_h[np.arange(n + 2), a] = 1
    return [list(a) for a in one_h]





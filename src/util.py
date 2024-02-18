from dataclasses import dataclass
import numpy as np
from typing import List, Type
from distributions import GBM

@dataclass()
class UserProfile:
    current_age: int
    goal_amount: int
    target_year: int
    current_balance: int
    current_income: float
    inflation_factor: float
    portfolio_return: float
    portfolio_stdv: float
    inflation_adjust: bool

def create_one_hot(n: int):
    """ return one hot vectors"""
    a = np.arange(n + 2)
    one_h = np.zeros([n+2, n+2])
    one_h[np.arange(n + 2), a] = 1
    return [list(a) for a in one_h]

def savings_fixed_policy(usr: Type[UserProfile], contrib=0.1, seed=None) -> List[float]:
    """ returns the projected annual balance from investment savings with fixed policy """
    annual_savings = list()
    for year_ in range(usr.target_year):
        if year_ > 0:
            usr.current_income = usr.current_income * (1 + usr.inflation_factor)
        this_year_saving = contrib * usr.current_income
        usr.current_balance = GBM(usr.current_balance, usr.portfolio_return
                                  , usr.portfolio_stdv).sample(seed)
        usr.current_balance += this_year_saving
        annual_savings.append(usr.current_balance)
    return annual_savings





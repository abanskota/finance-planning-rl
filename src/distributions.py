from abc import ABC, abstractmethod
import numpy as np
from dataclasses import dataclass
class Distribution(ABC):
    """an abstract class defining interfaces for probability distributions in general"""
    @abstractmethod
    def sample(self):
        pass

@dataclass
class GBM(Distribution):
    """ sampling from GBM distribution"""
    current_wealth: float
    ret: float # return
    stdv: float # std of returns

    def sample(self):
        rand_norm = np.random.normal()
        sig = np.sqrt(np.log(1 + (self.stdv/(1 + self.ret))**2))
        mu = np.log(1 + self.ret - ((sig ** 2) / 2))
        return self.current_wealth * np.exp(mu + rand_norm * self.stdv)

    
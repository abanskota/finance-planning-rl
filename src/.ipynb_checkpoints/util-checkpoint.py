from dataclasses import dataclass
import numpy as np

def create_one_hot(n: int):
    """ return one hot vectors"""
    a = np.arange(n + 2)
    one_h = np.zeros([n+2, n+2])
    one_h[np.arange(n + 2), a] = 1
    return [list(a) for a in one_h]

def retrieve_mu(ret, std):
    sig = np.sqrt(np.log(1 + (std/(1 + ret))**2))
    return np.log( 1 + ret - ((sig**2) / 2))

def retrieve_logn(ret, std):
    sig = np.sqrt(np.log(1 + (std/(1 + ret))**2))
    mu = np.log(1 + ret - ((sig ** 2) / 2))
    return mu, sig




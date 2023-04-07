import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 146155552 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    t = 77
    alpha = 1 - p
    min = (-x).min()
   
    z_2 = -np.log(1-p)/x.size    
    
    return 2*(-min-1/2)/(t*t), 2*(z_2-min-1/2)/(t*t)

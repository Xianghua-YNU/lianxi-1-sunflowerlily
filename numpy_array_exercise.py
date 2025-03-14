import numpy as np

def find_power_with_six():
    return np.array([i for i in range(1, 100) if str(2**i)[-1] == '6'])

def first_ten_powers():
    return np.array([2**i for i in range(10)])

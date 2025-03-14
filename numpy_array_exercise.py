import numpy as np

def find_power_with_six():
    return np.array([i for i in range(1, 100) if str(2**i)[-1] == '6'])

def first_ten_powers():
    return np.array([2**i for i in range(10)])

def create_frame_matrix():
    mat = np.zeros((10, 10))
    mat[0:2, :] = 1
    mat[-2:, :] = 1
    mat[:, 0:2] = 1
    mat[:, -2:] = 1
    return mat

def create_number_matrix():
    mat = np.full((10, 10), -1)
    mat[1:-1, 1:6] = np.arange(40).reshape(8, 5)
    return mat

def create_multiplication_matrix():
    return np.array([[i * j for j in range(5)] for i in range(3)])

def create_special_matrix():
    size = 11
    mat = np.ones((size, size))
    diag_vals = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]
    np.fill_diagonal(mat, diag_vals)
    return mat

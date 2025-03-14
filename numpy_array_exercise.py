import numpy as np

def find_power_with_six():
    """
    找出所有满足条件的i值(0<i<100)，使得2^i的最后一位数字是6
    
    返回:
    numpy.ndarray: 包含所有满足条件的i值的数组
    """
    a = [i for i in range(1,100) if str(2**i)[-1] == '6']
    return np.array(a)

def first_ten_powers():
    """
    计算2的前10次幂

    返回:
    numpy.ndarray: 包含2的前10次幂的数组
    """
    return np.array([2**i for i in range(10)])

def create_frame_matrix():
    """
    创建一个10x10的框架矩阵，边框为1，内部为0
    
    返回:
    numpy.ndarray: 10x10的框架矩阵
    """
    mat = np.ones((10, 10))
    
    # 使用切片操作填充中间区域为0
    # 行切片 2:-2 对应索引 2到7，列切片 2:-2 对应索引 2到7
    mat[2:-2, 2:-2] = 0
    
    return mat

def create_number_matrix():
    """
    创建一个10x10的数字矩阵，边框为-1，内部为0-39的数字
    
    返回:
    numpy.ndarray: 10x10的数字矩阵
    """
    # 创建 10x10 全-1矩阵
    mat = np.full((10, 10), -1.0)
    
    # 生成连续数字序列并填充中间区域
    numbers = np.arange(40).reshape(8, 5)  # 生成0-39的二维数组
    mat[1:-1, 1:6] = numbers  # 行切片1:-1对应第2-9行，列切片1:6对应第2-6列
    
    return mat

def create_multiplication_matrix():
    """
    创建一个3×5的矩阵，其中A[i,j] = i × j
    要求使用数组广播实现
    
    返回:
    numpy.ndarray: 3×5的矩阵
    """
    # 创建行向量 (3x1) 和列向量 (1x5)
    rows = np.arange(3).reshape(-1, 1)
    cols = np.arange(5)
    
    # 通过广播机制生成乘法表
    return (rows * cols).astype(float)

def create_special_matrix():
    # 创建 11x11 全1矩阵
    mat = np.ones((11, 11))
    
    # 生成对角线数值序列 [5,4,3,2,1,0,1,2,3,4,5]
    diag_values = np.concatenate([np.arange(5, -1, -1), np.arange(1, 6)])
    
    # 设置主对角线数值
    np.fill_diagonal(mat, diag_values)
    
    return mat

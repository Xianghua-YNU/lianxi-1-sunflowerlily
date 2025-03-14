import numpy as np

def calculate_declination_loop(days):
    """
    使用循环计算太阳赤纬
    
    参数:
    days (list): 需要计算的日期列表（距离1月1日的天数）
    
    返回:
    list: 对应日期的太阳赤纬值（度）
    """
    declinations = []
    for day in days:
        # 修正公式中的计算步骤
        declination = 23.44 * np.sin(np.radians((360/365.25) * (day - 81)))
        declinations.append(declination)
    
    return declinations

def calculate_declination_vector(days):
    """
    使用NumPy数组运算计算太阳赤纬
    
    参数:
    days (array-like): 需要计算的日期数组（距离1月1日的天数）
    
    返回:
    numpy.ndarray: 对应日期的太阳赤纬值（度）
    """
    # 使用NumPy数组运算计算太阳赤纬
    days_array = np.array(days)
    declinations = 23.44 * np.sin(np.radians((360/365.25) * (days_array - 81)))
    
    return declinations

def compare_solstices_equinoxes():
    """
    比较春分、秋分、夏至、冬至时的太阳赤纬值
    打印使用循环和数组运算两种方法的计算结果
    
    返回:
    None
    """
    # 特殊日期（距离1月1日的天数）
    special_days = [79, 172, 266, 356]  # 春分、夏至、秋分、冬至
    
    # 使用循环计算太阳赤纬
    declinations_loop = calculate_declination_loop(special_days)
    print("使用循环计算的太阳赤纬值:", declinations_loop)
    
    # 使用NumPy数组运算计算太阳赤纬
    declinations_vector = calculate_declination_vector(special_days)
    print("使用NumPy数组运算计算的太阳赤纬值:", declinations_vector)

if __name__ == "__main__":
    compare_solstices_equinoxes()

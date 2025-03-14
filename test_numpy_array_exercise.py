import unittest
import numpy as np
from numpy_array_exercise import (
    find_power_with_six, 
    first_ten_powers
)

class TestNumpyPowerExercise(unittest.TestCase):
    def test_find_power_with_six(self):
        """测试2^i末尾为6的i值查找函数"""
        result = find_power_with_six()
    
        # 检查返回类型是否为numpy数组
        self.assertIsInstance(result, np.ndarray)
            
        # 检查是否包含了所有满足条件的数
        all_valid = np.array([i for i in range(1, 100) if str(2**i)[-1] == '6'])
        np.testing.assert_array_equal(sorted(result), sorted(all_valid))

    def test_first_ten_powers(self):
        """测试2的前10次幂计算函数"""
        result = first_ten_powers()
        
        # 检查返回类型是否为numpy数组
        self.assertIsInstance(result, np.ndarray)
        
        # 检查数组长度是否为10
        self.assertEqual(len(result), 10)
        
        # 检查计算结果是否正确
        expected = np.array([2**i for i in range(10)])
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()

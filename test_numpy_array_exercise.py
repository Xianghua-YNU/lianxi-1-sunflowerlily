import unittest
import numpy as np
from numpy_array_exercise import (
    find_power_with_six
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
if __name__ == '__main__':
    unittest.main()

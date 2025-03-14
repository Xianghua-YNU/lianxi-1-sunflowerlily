import numpy as np
import matplotlib.pyplot as plt

def plot_deltoid(num_points=1000):
    """
    绘制三角洲曲线
    x = 2cos(θ) + cos(2θ)
    y = 2sin(θ) - sin(2θ)
    
    参数:
    num_points (int): 采样点数，默认1000
    """
    # 输入验证
    if num_points <= 0:
        raise ValueError("采样点数必须为正整数")
        
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = 2 * np.cos(theta) + np.cos(2 * theta)
    y = 2 * np.sin(theta) - np.sin(2 * theta)
    
    plt.figure()  # 创建新图形
    plt.plot(x, y, color='blue', linewidth=2)
    plt.title('Deltoid Curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    # 使用 plt.gca().set_aspect('equal') 替代 plt.axis('equal')
    plt.gca().set_aspect('equal')
    
    return x, y  # 返回计算结果供测试使用

def plot_galilean_spiral(num_points=1000):
    """
    绘制伽利略螺旋
    r = θ²
    
    参数:
    num_points (int): 采样点数，默认1000
    """
    # 输入验证
    if num_points <= 0:
        raise ValueError("采样点数必须为正整数")
        
    theta = np.linspace(0, 6 * np.pi, num_points)
    r = theta ** 2
    
    plt.figure()  # 创建新图形
    ax = plt.subplot(111, projection='polar')
    ax.plot(theta, r, color='#FF6F61', linewidth=1.8)
    # 确保调用 plt.plot
    plt.plot(theta, r, color='#FF6F61', linewidth=1.8)
    plt.title('Galilean Spiral (r = θ²)', pad=20)
    ax.grid(True, alpha=0.4)
    
    # 调整极坐标轴标签位置
    ax.set_rlabel_position(225)
    ax.set_theta_zero_location('N')
    
    return theta, r  # 返回计算结果供测试使用

def plot_feys_function(num_points=2000):
    """
    绘制Fey's函数
    r = exp(cos(θ)) - 2cos(4θ) + sin⁵(θ/12)
    
    参数:
    num_points (int): 采样点数，默认2000
    """
    # 输入验证
    if num_points <= 0:
        raise ValueError("采样点数必须为正整数")
        
    theta = np.linspace(0, 2 * np.pi, num_points)
    r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + np.power(np.sin(theta / 12), 5)
    
    plt.figure()  # 创建新图形
    ax = plt.subplot(111, projection='polar')
    ax.plot(theta, r, color='#6A0DAD', linewidth=1.5)
    # 确保调用 plt.plot
    plt.plot(theta, r, color='#6A0DAD', linewidth=1.5)
    plt.title("Fey's Function", pad=20)
    ax.grid(True, alpha=0.5)
    
    # 设置极坐标显示参数
    ax.set_rlabel_position(135)
    ax.set_theta_zero_location('E')
    ax.set_facecolor('#F8F8FF')  # 设置背景色为幽灵白
    
    return theta, r  # 返回计算结果供测试使用

def save_plots():
    """
    生成并保存所有图形
    """
    # 设置图形大小和DPI
    plt.figure(figsize=(10, 8), dpi=100)
    
    # 绘制并保存三角洲曲线
    plot_deltoid()
    plt.savefig('deltoid.png')
    plt.close()
    
    # 绘制并保存伽利略螺旋
    plot_galilean_spiral()
    plt.savefig('galilean_spiral.png')
    plt.close()
    
    # 绘制并保存Fey's函数
    plot_feys_function()
    plt.savefig('feys_function.png')
    plt.close()

if __name__ == "__main__":
    save_plots()

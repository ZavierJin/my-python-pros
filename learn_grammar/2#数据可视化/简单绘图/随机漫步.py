# learn python -- 13th day
""" 随机漫步 """
import matplotlib.pyplot as plt
from random import choice


class RandomWalk():
    """
    随机漫步

    num_points 总次数
    x_values, y_values  x,y坐标列表
    """
    def __init__(self, num_points=5000):
        self.num_points = num_points
        # 创建x, y坐标列表，初始点是原点
        self.x_values = [0]
        self.y_values = [0]

    # 随机生成方向和步数
    def get_step(self):
        direct = choice([1, -1])
        dist = choice(list(range(5)))
        return direct * dist

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表达到指定长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step()

            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x, y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


def main():
    while True:
        # 创建一个随机漫步实例
        rw = RandomWalk(50000)
        rw.fill_walk()

        # 设置绘图窗口的尺寸
        plt.figure(figsize=(8, 7))

        point_nums = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_values, c=point_nums,
                    cmap=plt.cm.Greens, s=1)
        plt.title("Random Walk", fontsize=25)

        # 突出起点和终点
        plt.scatter(0, 0, c='yellow', s=20)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', s=20)

        # 隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()

        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break


if __name__ == '__main__':
    main()

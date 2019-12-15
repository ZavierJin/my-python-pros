# learn python -- 14th day

""" Pygal """

from random import randint
import pygal


class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


def main():
    die_1 = Die(6)
    die_2 = Die(10)
    roll_times = 50000

    results = []
    for i in range(roll_times):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # 分析结果
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(1, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # 对结果进行可视化分析（Bar为直方图）
    hist = pygal.HorizontalBar()    # 横向

    hist.title = "Results of rolling two D6 1000 times. (in %)"
    # hist.x_labels = [str(num) for num in range(2, max_result+1)]
    hist.x_title = 'Result'
    hist.y_title = "Frequency of Result"

    # 数据添加
    for num in range(2, max_result+1):
        hist.add(str(num), frequencies[num-1])

    # 渲染，实现图表交互
    hist.render()

    # 保存到文件(.svg类型，可用浏览器打开)
    hist.render_to_file('die_visual.svg')


if __name__ == '__main__':
    main()

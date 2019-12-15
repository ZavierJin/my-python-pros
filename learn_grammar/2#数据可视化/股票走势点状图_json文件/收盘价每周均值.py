# learn python -- 18th day


""" 收盘价均值 """
import json
import pygal
import math
from itertools import groupby


def read_data():
    # 将数据加载到一个字典中
    filename = 'btc_close_2017.json'
    with open(filename, 'r', encoding='utf-8') as f:
        btc_data = json.load(f)

    # 读取数据
    dates, months, weeks, weekdays, closes = [], [], [], [], []
    for btc_dict in btc_data:
        dates.append(btc_dict['date'])
        months.append(int(btc_dict['month']))
        weeks.append(int(btc_dict['week']))
        weekdays.append(btc_dict['weekday'])
        # 注：数据类型不一，需先转化为浮点数
        closes.append(int(float(btc_dict['close'])))


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


def second_pro():
    # 将数据加载到一个字典中
    filename = 'btc_close_2017.json'
    with open(filename, 'r', encoding='utf-8') as f:
        btc_data = json.load(f)

    # 读取数据
    dates, months, weeks, weekdays, closes = [], [], [], [], []
    for btc_dict in btc_data:
        dates.append(btc_dict['date'])
        months.append(int(btc_dict['month']))
        weeks.append(int(btc_dict['week']))
        weekdays.append(btc_dict['weekday'])
        # 注：数据类型不一，需先转化为浮点数
        closes.append(int(float(btc_dict['close'])))

    # 只取2~11月每周均值数据
    idx_week = dates.index('2017-12-11')
    draw_line(weeks[1:idx_week], closes[1:idx_week],
        '收盘价每周均值', '周日均值')


"""
def first_pro():

    # 创建图表对象
    line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
    line_chart.title = '收盘价对数变换（￥）'
    line_chart.x_labels = dates
    # x轴天数间隔20天
    day_interval = 20
    line_chart.x_labels_major = dates[::day_interval]
    # 绘制
    closes_log = [math.log10(_) for _ in closes]    # 对数变换
    line_chart.add('log收盘价', closes_log)
    # 存入文件
    line_chart.render_to_file('收盘价对数变换折线图.svg')
"""

if __name__ == '__main__':
    second_pro()

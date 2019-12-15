# learn python -- 17th day


""" 对数变换 """
import json
import pygal
import math


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

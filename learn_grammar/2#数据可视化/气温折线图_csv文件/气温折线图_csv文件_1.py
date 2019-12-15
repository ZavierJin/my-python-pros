# learn python -- 17th day

""" 气温折线图  文件数据导入及绘制 """

import csv  # csv文件
from matplotlib import pyplot as plt
from datetime import datetime   # 时间模块


""" 从文件中获取最高气温 """
fn = 'sitka_weather_2014.csv'
with open(fn) as f:
    # 创建文件对象
    reader = csv.reader(f)
    # 创建行对象
    header_row = next(reader)
    # 读取日期、最高和最低气温
    dates, highs, lows = [], [], []   # 多个定义
    for row in reader:
        cur_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(cur_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

""" 根据数据绘制图形 """
fig = plt.figure(dpi=128, figsize=(5, 3))
plt.plot(dates, highs, c='red', alpha=0.5)  # alpha为透明度
plt.plot(dates, lows, c='blue', alpha=0.5)
# 填充中间区域
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

""" 设置图形格式 """
plt.title("Daily High And Low Temperatures - 2014", fontsize=18)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()     # 绘制斜日期标签
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()

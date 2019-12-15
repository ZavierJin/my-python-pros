# learn python -- 17th day


# """ 网上下载文件方式#1 """
# from __future__ import (absolute_import, division,
#                         print_function, unicode_literals)
# from urllib.request import urlopen
# import json


# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = urlopen(json_url)  # 2
# # 读取数据
# req = response.read()
# # 将数据写入文件
# with open('btc_close_2017_urllib.json', 'wb') as f:  # 3
#     f.write(req)
# # 加载json格式
# file_urllib = json.loads(req.decode('utf8'))  # 4
# print(file_urllib)


""" 网上下载文件方式#2 """
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)  # 1
# 将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)  # 2
# 读取json格式
file_requests_1 = req.json()  # 3

print(file_requests_1)

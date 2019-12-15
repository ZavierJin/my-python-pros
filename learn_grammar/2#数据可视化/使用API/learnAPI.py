# learn python -- 18th day

"""
使用API
从github上获取信息
用pygal进行可视化
"""


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

# 执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)    # 是否读取成功

# 将API响应储存在一个变量中
response_dict = r.json()
print('Total responsitories: ', response_dict['total_count'])

# 探索有关仓库的信息
item_dicts = response_dict['items']

# 根据id排序，用operator模块中的itemgetter函数提取对应键的值
item_dicts = sorted(item_dicts, key=itemgetter('id'),
                    reverse=True)

names, plot_dicts = [], []
wrong_idxs = []     # 记录有内容空缺的项目下标
for item_dict in item_dicts:
    plot_dict = {
        'value': item_dict['stargazers_count'],
        'label': item_dict['description'],
        'xlink': item_dict['html_url']
    }

    if not plot_dict['label']:  # 防止出现None的情况
        plot_dict['label'] = 'None'
        wrong_idx = item_dicts.index(item_dict)
        print(str(wrong_idx) + ' wrong.')
        wrong_idxs.append(wrong_idx)

    plot_dicts.append(plot_dict)
    names.append(item_dict['name'])


# 可视化
# 颜色配置
my_style = LS('#333366', base_style=LCS)
# 其他配置
my_config = pygal.Config()
my_config.x_label_rotation = 45         # x轴标签旋转
my_config.show_legend = False           # 隐藏图例
my_config.title_font_size = 24
my_config.label_font_size = 14          # 副标签
my_config.major_label_font_size = 18    # 主标签
my_config.truncate_label = 15           # 标签长度限制
my_config.show_y_guides = False         # 不显示水平线
my_config.width = 1000                  # 自定义宽度


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Python Projects on Github'
chart.x_labels = names


chart.add('', plot_dicts)
chart.render_to_file('python_star_4.svg')

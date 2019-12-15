

import requests



# 执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# 将API响应储存在一个变量中
response_dict = r.json()
print('Total responsitories: ', response_dict['total_count'])

# 探索有关仓库的信息
item_dicts = response_dict['items']

count = 1
for item_dict in item_dicts:
    print(count)
    print("\nName:\n\t", item_dict['name'])
    print('\t' + str(item_dict['watchers_count']))
    count += 1

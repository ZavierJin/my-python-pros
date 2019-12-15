# learn python -- 15th day

""" 排序测试 """

import my_sort as st
from random import randint
import json


def store_data(num_min=1, num_max=100, amount=1000):
    with open("my_data.json", 'w', encoding='utf-8') as fn:
        data_list = []
        for i in range(amount):
            data_list.append(randint(num_min, num_max))
        json.dump(data_list, fn)


def load_data():
    with open("my_data.json", 'r', encoding='utf-8') as fn:
        data_list = json.load(fn)
    return data_list


def show(my_list):
    for i in range(len(my_list)):
        print("%3d" % my_list[i], end=' ')
        if i % 10 == 9:
            print()


if __name__ == '__main__':
    data_list = load_data()
    str1 = " Original Data "
    print(str1.center(40, '-'))
    show(data_list)

    new_list = st.select_sort(data_list)

    str2 = " New Data "
    print(str2.center(40, '-'))
    show(new_list)

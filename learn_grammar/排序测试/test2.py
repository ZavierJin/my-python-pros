# learn python -- 15th day

"""
排序测试
用类的形式定义
"""

import my_sort as st
from random import randint
import json


class My_Data():
    """ 数据 """
    def __init__(self, num_min=1, num_max=100, amount=1000):
        self.num_min = num_min
        self.num_max = num_max
        self.amount = amount
        self.data_list = []

    def refresh_data(self, new_list=[]):
        """ 更新数据，如果没有传入形参则随机生成"""
        if not new_list:
            self.data_list = []
            for i in range(self.amount):
                self.data_list.append(randint(self.num_min, self.num_max))
        else:
            self.data_list = new_list

    def store_data(self):
        with open("my_data.json", 'w', encoding='utf-8') as fn:
            json.dump(self.data_list, fn)

    def load_data(self):
        self.data_list = []
        with open("my_data.json", 'r', encoding='utf-8') as fn:
            self.data_list = json.load(fn)

    def display(self):
        for i in range(len(self.data_list)):
            print("%3d" % self.data_list[i], end=' ')
            if i % 10 == 9:
                print()


if __name__ == '__main__':
    test2 = My_Data(-50, 70)
    test2.refresh_data()
    test2.store_data()

    # display
    str1 = " Original Data "
    print(str1.center(40, '-'))
    test2.display()

    new_list = st.select_sort(test2.data_list)
    test2.refresh_data(new_list)

    str2 = " New Data "
    print(str2.center(40, '-'))
    test2.display()

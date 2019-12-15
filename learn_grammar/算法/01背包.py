"""
dynamic programming
0/1背包问题
"""
from random import randint

num_call = 0    # 全局变量，记录函数调用次数


def MaxVal(weights, values, cur_index, knap_sur):
    """
    0/1背包基础算法

    :param weights: 重量列表
    :param values: 价格列表
    :param cur_index: 当前物品下标（0~n-1）
    :param knap_sur: 背包剩余重量
    :return: 当前结点决策的最大值
    """
    global num_call
    num_call += 1
    # print("cur_index = %d, knap_sur = %d" % (cur_index, knap_sur))
    # 递归出口
    if cur_index == 0:
        if weights[cur_index] <= knap_sur:
            return values[cur_index]
        else:
            return 0
    # 左结点，不装
    without_index = MaxVal(weights, values, cur_index-1, knap_sur)
    # 右结点，装
    if weights[cur_index] <= knap_sur:
        with_index = MaxVal(weights, values, cur_index-1,
                            knap_sur-weights[cur_index]) + values[cur_index]
        return max(with_index, without_index)
    else:   # 装不下
        return without_index


def FastMaxVal(weights, values, cur_index, knap_sur, stores):
    """ 改良版递归部分，空间换时间，避免重叠子问题 """
    global num_call
    num_call += 1
    try:
        node_val = stores[(cur_index, knap_sur)]
        return node_val
    except KeyError:
        if cur_index == 0:
            if weights[cur_index] <= knap_sur:
                stores[(cur_index, knap_sur)] = values[cur_index]
                return values[cur_index]
            else:
                stores[(cur_index, knap_sur)] = 0
                return 0
        # 左结点，不装
        without_index = FastMaxVal(weights, values, cur_index-1, knap_sur,
            stores)
        # 右结点，装
        if weights[cur_index] <= knap_sur:
            with_index = FastMaxVal(weights, values, cur_index-1,
                knap_sur-weights[cur_index], stores) + values[cur_index]
            node_val = max(with_index, without_index)
            stores[(cur_index, knap_sur)] = node_val
            return node_val
        else:   # 装不下
            stores[(cur_index, knap_sur)] = without_index
            return without_index


def MaxVal2(weights, values, cur_index, knap_sur):
    """ 改良版 """
    stores = {}
    return FastMaxVal(weights, values, cur_index, knap_sur, stores)


def test1():
    """ 测试 """
    global num_call
    item_total = 20     # 可选物品总数
    knap = 45   # 物品最大重量
    weights, values = [], []
    # 随机生成物品，并显示
    for i in range(item_total):
        weight = randint(1, 10)
        value = randint(2, 9)
        print("(%d, %d)" % (weight, value), end='\t')
        weights.append(weight)
        values.append(value)
        if (i+1) % 10 == 0:
            print()
    print()

    num_call = 0
    max_val = MaxVal(weights, values, item_total-1, knap)
    print("Original:")
    print("max_val = %d, num_call = %d" % (max_val, num_call))
    num_call = 0
    max_val = MaxVal2(weights, values, item_total-1, knap)
    print("Fast:")
    print("max_val = %d, num_call = %d" % (max_val, num_call))


if __name__ == '__main__':
    test1()


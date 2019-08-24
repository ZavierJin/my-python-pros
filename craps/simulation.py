""" Simulation """
from model import craps_game
import matplotlib.pyplot as plt


def simulation(sim_times=100, start_money=1000, debt=50, count_max=20):
    over_times = 0
    count_list, money_list = [], []
    for _ in range(sim_times):
        is_over, count, re_money = craps_game(start_money, debt, count_max)
        if is_over:
            over_times += 1
        count_list.append(count)
        money_list.append(re_money)

    return over_times, count_list, money_list


def show_remain_money(money_list, sim_times=100, start_money=1000,
                      count_max=20):
    plt.title("Remain Money (start from %d, try %d times)" % (start_money,
        count_max))
    plt.ylabel("Money")
    plt.xlabel("Times")
    x = list(range(1, sim_times+1))
    y = sorted(money_list)
    # y = money_list
    line_y = [start_money for _ in range(sim_times)]
    plt.plot(x, line_y, c='red')
    plt.plot(x, y, c='red', alpha=0.5)
    plt.fill_between(x, y, facecolor='red', alpha=0.1)
    plt.show()


def test():
    sim_times = 1000
    start_money = 1000
    debt = 50
    count_max = 10
    over_times, count_list, money_list = simulation(sim_times, start_money,
        debt, count_max)
    show_remain_money(money_list, sim_times, start_money, count_max)


if __name__ == '__main__':
    test()

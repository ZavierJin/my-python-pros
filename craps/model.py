""" Model """
from random import randint


def craps_game(start_money=1000, debt=50, count_max=20):
    my_money = start_money
    over = False
    count = 0

    while (not over) and (count < count_max):
        need_go_on = False
        count += 1

        # 第一次
        one = randint(1, 6)
        two = randint(1, 6)
        current = one + two
        if current == 7 or current == 11:
            my_money += debt
        elif current == 2 or current == 3 or current == 12:
            my_money -= debt
        else:
            need_go_on = True

        # 循环加注环节
        if need_go_on:
            pres = []
            total_debt = debt
        while need_go_on:
            # 无法加注
            if need_go_on and my_money <= total_debt:
                my_money -= total_debt
                break

            # 加注
            pres.append(current)
            total_debt += debt

            # 继续
            one = randint(1, 6)
            two = randint(1, 6)
            current = one + two
            if current == 7:
                my_money -= total_debt
                need_go_on = False
            else:
                for pre in sorted(pres):
                    differ = current - pre
                    if differ == 1 or differ == -1:
                        my_money -= total_debt
                        need_go_on = False
                        break
                    elif differ == 0:
                        my_money += total_debt
                        need_go_on = False
                        break

        # 是否出局
        if my_money <= 0:
            over = True

    return over, count, my_money


def test():
    sim_times = 10
    over_times = 0
    count_list, money_list = [], []
    for _ in range(sim_times):
        is_over, count, re_money = craps_game()
        if is_over:
            over_times += 1
        count_list.append(count)
        money_list.append(re_money)

    print(money_list)


if __name__ == "__main__":
    test()

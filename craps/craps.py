
"""
Craps赌博游戏_改编版
by jzy

每轮开始 玩家下注 摇两颗色子
如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜
其他情况本轮游戏进入循环加注环节
循环加注环节中 玩家若不加注则视作放弃 庄家胜
玩家加注后 再次摇两颗色子
如果摇出7点 庄家胜
如果摇出已出现的点数 玩家胜
如果摇出点数与已出现点数相差为1 庄家胜
否则此环节继续 玩家继续摇色子
"""

from random import randint

start_money = 1000
my_money = start_money
over = False
count = 0

print("\n----- Craps赌博游戏_改编版 -----")

# 游戏帮助
print("\n游戏帮助：")
helps = (
    "每轮开始，玩家下注后摇两颗色子",
    "如果第一次摇出 7 点或 11 点，则玩家胜",
    "如果摇出 2 点、 3 点或 12 点，则庄家胜",
    "其他情况则本轮游戏进入循环加注环节",
    "在循环加注环节中，玩家若不加注则视作放弃，庄家胜",
    "玩家加注后，再次摇两颗色子",
    "如果摇出 7 点，则庄家胜",
    "如果摇出已出现的点数，则玩家胜",
    "如果摇出点数与已出现点数相差为 1 ，则庄家胜",
    "其他情况则循环加注环节继续",
    "玩家在每轮开始不下注可以退出游戏",
    "玩家若资产为 0 ，则出局",
    )
for mess in helps:
    print("\t" + mess)

while not over:
    need_go_on = False
    count += 1
    # 下注
    print("\n------- 第 %d 轮 -------\n" % count)
    print("你的当前资产为： %d" % my_money)
    while True:
        debt = int(input("请下注：（必须为 50 的倍数，下注为 \
0 则结束游戏）\n"))
        if debt > 0 and debt <= my_money and debt % 50 == 0:
            print("成功下注 %d 元。" % debt)
            break
        elif debt == 0:
            print("\n成功结束游戏。")
            over = True
            break
        elif debt > my_money:
            print("\n抱歉，你没有那么多钱。")
        else:
            print("\n无效下注。")
    if over:  # 玩家选择结束游戏
        break

    # 第一次
    one = randint(1, 6)
    two = randint(1, 6)
    current = one + two
    print("\n你掷了两个骰子 ... %d ... %d" % (one, two))
    print("你摇出了 %d 点。" % current)
    if current == 7 or current == 11:
        print("玩家胜，你赢得了 %d 元！" % debt)
        my_money += debt
    elif current == 2 or current == 3 or current == 12:
        print("庄家胜，你输掉了 %d 元。" % debt)
        my_money -= debt
    else:
        print("进入循环加注环节！")
        need_go_on = True

    # 循环加注环节
    if need_go_on:
        pres = []
        print("\n----- 循环加注环节 -----\n")
    while need_go_on:
        # 无法加注
        if need_go_on and my_money <= debt:
            print("\n你的钱包空空，无法加注。")
            print("庄家胜，你输掉了 %d 元。" % debt)
            my_money -= debt
            break

        # 加注
        pres.append(current)
        print("你的当前资产为： %d 。当前总下注： %d" % (my_money, debt))
        print("你掷过的点数有：", end="")
        print(sorted(pres))
        while True:
            cur_debt = int(input("请加注：（必须为 50 的倍数，加注\
为 0 则庄家自动获胜）\n"))
            if cur_debt > 0 and cur_debt + debt <= my_money \
                and cur_debt % 50 == 0:
                debt += cur_debt
                print("成功加注 %d 元，当前总下注 %d 元。" % (cur_debt, debt))
                break
            elif cur_debt == 0:     # 停止加注
                print("\n停止加注，庄家胜，你输掉了 %d 元。" % debt)
                my_money -= debt
                need_go_on = False
                break
            elif cur_debt + debt > my_money:
                print("\n抱歉，你没有那么多钱。")
            else:
                print("\n无效下注。")
        if not need_go_on:
            break

        # 继续
        one = randint(1, 6)
        two = randint(1, 6)
        current = one + two
        print("\n你掷了两个骰子 ... %d ... %d" % (one, two))
        print("你摇出了 %d 点。" % current)
        if current == 7:
            print("庄家胜，你输掉了 %d 元。" % debt)
            my_money -= debt
            need_go_on = False
        else:
            for pre in sorted(pres):
                differ = current - pre
                if differ == 1 or differ == -1:
                    print("%d 与 %d 只相差 1" % (current, pre))
                    print("庄家胜，你输掉了 %d 元。" % debt)
                    my_money -= debt
                    need_go_on = False
                    break
                elif differ == 0:
                    print("玩家胜，你赢得了 %d 元！" % debt)
                    my_money += debt
                    need_go_on = False
                    break

        if need_go_on:
            print("游戏继续。\n")

    # 是否出局
    if my_money <= 0:
        print("\n抱歉，你已出局。")
        over = True

# 结算
print("\n------- 结算 -------\n")
print("游戏结束，你共进行了 %d 轮。" % count)
if my_money <= 0:
    print("真遗憾，你输光了所有的钱。")
elif my_money <= start_money:
    print("幸好溜得早，你只剩下了 %d 元。" % my_money)
elif my_money <= start_money + 500:
    print("运气不错，你赢了 %d 元，总资产有 %d 元。" % \
        (my_money - start_money, my_money))
elif my_money <= 2*start_money:
    print("水平不错！你赢了 %d 元，总资产有 %d 元。" % \
        (my_money - start_money, my_money))
else:
    print("天哪，你是赌神吧！你赢了 %d 元，总资产有 %d 元！" % \
        (my_money - start_money, my_money))

input()

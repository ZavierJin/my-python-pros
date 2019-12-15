# 跑马灯 Character Horse Lantern

from os import system
from time import sleep


def main():
    content = "浙江台州黄岩是个好地方…………"
    while True:
        # 清理屏幕上的输出
        system('cls')   # system('clear')
        print(content)
        # 休眠200ms
        sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()

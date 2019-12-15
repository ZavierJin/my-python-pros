"""多进程"""
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print("启动下载进程，进程号【%d】。" % getpid())
    print("开始下载【%s】..." % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("【%s】下载完成！耗时 %d 秒" % (filename, time_to_download))


def main():
    start_time = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('老人与海.pdf', ))
    p2.start()
    p1.join()
    p2.join()
    end_time = time()
    print("总共耗时 %d 秒" % (end_time - start_time))


if __name__ == '__main__':
    main()

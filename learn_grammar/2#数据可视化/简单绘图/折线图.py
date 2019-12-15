# learn python -- 12th day
import matplotlib.pyplot as plt


def main():
    input_values = list(range(1, 5+1))
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)

    # 设置图表标题，并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    # 设置刻度标记大小
    plt.tick_params(axis='both', labelsize=14)

    plt.show()


if __name__ == '__main__':
    main()

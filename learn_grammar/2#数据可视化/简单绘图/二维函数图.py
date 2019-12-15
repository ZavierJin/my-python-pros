# learn python -- 13th day
import matplotlib.pyplot as plt


def main():
    x_values = list(range(1, 1000+1))
    y_values = [x**2 for x in x_values]

    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens,
                edgecolor='none', s=40)

    plt.title("SSS", fontsize=24)
    plt.xlabel("VV", fontsize=14)
    plt.ylabel("YYY", fontsize=14)

    plt.tick_params(axis='both', which='major', labelsize=14)
    # 设置坐标轴取值范围
    plt.axis([0, 1100, 0, 1100000])

    plt.show()


if __name__ == '__main__':
    main()

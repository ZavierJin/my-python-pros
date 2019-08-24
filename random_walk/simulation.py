""" simulation """
from model import Player
import matplotlib.pyplot as plt
import numpy as np


def one_trial(walk_times):
    """ one trial of random walk """
    player = Player('Mike')
    distances = []
    # x_list, y_list = [], []

    for _ in range(walk_times):
        player.move()
        # x, y = p1.get_loc()
        # x_list.append(x)
        # y_list.append(y)
        distances.append(player.get_dist())

    end_x, end_y = player.get_loc()

    return distances, end_x, end_y


def simulation(sim_times, walk_times):
    """ many times trial """
    dist_list = []
    aver_dist = []
    x_list, y_list = [], []

    for _ in range(sim_times):
        distances, end_x, end_y = one_trial(walk_times)
        x_list.append(end_x)
        y_list.append(end_y)
        dist_list.append(distances)

    # data processing
    for j in range(walk_times):
        dist_sum = 0
        for i in range(sim_times):
            dist_sum += dist_list[i][j]
        aver_dist.append(dist_sum/sim_times)

    return aver_dist, x_list, y_list


def show_ter_pos(x_list, y_list):
    """ show the terminal position """
    plt.title("Terminal Position of 500 Random Walks")
    plt.xlabel("X")
    plt.ylabel("Y")
    x = np.array(x_list)
    y = np.array(y_list)
    color_list = np.sqrt(x**2 + y**2)
    plt.scatter(x_list, y_list, s=30, c=color_list, marker=(5, 1))
    plt.show()


def test():
    aver_dist, x_list, y_list = simulation(100, 500)
    show_ter_pos(x_list, y_list)


if __name__ == '__main__':
    test()

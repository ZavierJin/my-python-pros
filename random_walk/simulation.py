""" simulation """
from model import Player, SEPlayer, LoveNorthPlayer
import matplotlib.pyplot as plt
import numpy as np


def one_trial(walk_times):
    """ one trial of random walk """
    # player = Player('Mike')
    player = LoveNorthPlayer('Bob')
    distances = [0]

    for _ in range(walk_times):
        player.move()
        distances.append(player.get_dist())

    end_x, end_y = player.get_loc()

    return distances, end_x, end_y


def simulation(sim_times, walk_times):
    """ many times trial """
    dist_list = []
    aver_dist = []
    x_list, y_list = [0], [0]

    for _ in range(sim_times):
        distances, end_x, end_y = one_trial(walk_times)
        x_list.append(end_x)
        y_list.append(end_y)
        dist_list.append(distances)

    # data processing
    for j in range(walk_times+1):
        dist_sum = 0
        for i in range(sim_times):
            dist_sum += dist_list[i][j]
        aver_dist.append(dist_sum/sim_times)

    return aver_dist, x_list, y_list


def show_ter_pos(x_list, y_list):
    """ show the terminal position """
    plt.title("Terminal Position of 30 Random Walks")
    plt.xlabel("X")
    plt.ylabel("Y")
    x = np.array(x_list)
    y = np.array(y_list)
    color_list = np.sqrt(x**2 + y**2)
    plt.scatter(x_list, y_list, s=30, c=color_list, marker=(5, 1))
    plt.scatter(0, 0, s=40, c='black')
    plt.show()


def show_aver_dist(aver_dist, walk_times):
    """ show average distance of each walk """
    plt.title("Average Distance of Each Walk")
    plt.xlabel("Walks")
    plt.ylabel("Distance")
    x = list(range(1, walk_times+2))
    plt.plot(x, aver_dist, c='red', alpha=0.5)
    plt.fill_between(x, aver_dist, facecolor='red', alpha=0.1)
    plt.show()


def test():
    sim_times = 100
    walk_times = 500
    aver_dist, x_list, y_list = simulation(sim_times, walk_times)
    # show_ter_pos(x_list, y_list)
    show_aver_dist(aver_dist, walk_times)


if __name__ == '__main__':
    test()

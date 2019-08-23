""" simulation """
from model import Player
import pylab


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

    return distances


def simulation(sim_times, walk_times):
    """ many times trial """
    dist_list = []
    aver_dist = []

    for _ in range(sim_times):
        dist_list.append(one_trial(walk_times))

    # data processing
    for j in range(walk_times):
        dist_sum = 0
        for i in range(sim_times):
            dist_sum += dist_list[i][j]
        aver_dist.append(dist_sum/sim_times)

    return aver_dist


def data_visual(aver_dist):
    """ show the data """
    pylab.plot(aver_dist)
    pylab.show()


def average_dist_test():
    aver_dist = simulation(1000, 500)
    data_visual(aver_dist)


if __name__ == '__main__':
    average_dist_test()

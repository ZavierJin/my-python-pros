""" Model """

from random import choice
from math import sqrt


class Point(object):
    """ point on the map """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_xy(self):
        """ get point x and y """
        return self.x, self.y

    def get_dist(self):
        """ get distance from point to origin """
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)


class Compass(object):
    """ direction and distance of the next movement """
    # poss_dire = ['N', 'S', 'W', 'E']

    def __init__(self, p_type):
        self.p_type = p_type
        self.tx = 0
        self.ty = 0
        self.tdist = 1
        if p_type == 'normal':
            self.poss_dire = ['N', 'S', 'W', 'E']
        elif p_type == 'swe':
            # SWEPlayer
            self.poss_dire = ['S', 'W', 'E']
        elif p_type == 'se':
            # SEPlayer
            self.poss_dire = ['S', 'E']
        else:
            self.poss_dire = ['N', 'S', 'W', 'E']

    def get_dire(self):
        """ get tx and ty """
        return self.tx, self.ty

    # def get_tdist(self):
    #     """ get distance of movement """
    #     return self.tdist

    def update_dire(self):
        """ update direction """
        dire = choice(self.poss_dire)
        if dire == 'N':
            if self.p_type == 'ln':
                self.tx, self.ty = (0, 2 * self.tdist)
            else:
                self.tx, self.ty = (0, self.tdist)
        elif dire == 'S':
            self.tx, self.ty = (0, -self.tdist)
        elif dire == 'W':
            self.tx, self.ty = (-self.tdist, 0)
        elif dire == 'E':
            self.tx, self.ty = (self.tdist, 0)
        else:
            raise ValueError("In Compass, get_dire")


class Map(object):
    """ Map """
    def __init__(self, p_type):
        self.p_type = p_type

    def move_point(self, old_point, compass):
        ox, oy = old_point.get_xy()
        tx, ty = compass.get_dire()
        ox += tx
        oy += ty
        return Point(ox, oy)


class Player(object):
    """ Player """
    def __init__(self, name='unknown', p_type='normal'):
        self.name = name
        self.p_type = p_type
        self.map = Map(p_type)
        self.location = Point(0, 0)
        self.compass = Compass(p_type)
        self.distance = 0

    def get_name(self):
        return self.name

    def print_loc(self):
        print(self.location)

    def get_loc(self):
        return self.location.get_xy()

    def get_dist(self):
        return self.distance

    def move(self):
        self.compass.update_dire()
        self.location = self.map.move_point(self.location, self.compass)
        self.distance = self.location.get_dist()


class SEPlayer(Player):
    """ SE player, cannot go north and west """
    def __init__(self, name):
        super().__init__(name, 'se')


class SWEPlayer(Player):
    """ SWE player, cannot go north"""
    def __init__(self, name):
        super().__init__(name, 'swe')


class LoveNorthPlayer(Player):
    """ love north player, go north fast"""
    def __init__(self, name):
        super().__init__(name, 'ln')


def test():
    walk_times = 3
    p1 = SWEPlayer('John')
    p2 = SWEPlayer('John')
    print(p1.get_dist())
    distances = []
    x_list, y_list = [], []
    for _ in range(walk_times):
        p1.move()
        x, y = p1.get_loc()
        x_list.append(x)
        y_list.append(y)
        distances.append(p1.get_dist())

    print(distances)
    print(x_list)
    print(y_list)
    distances = []
    x_list, y_list = [], []

    for _ in range(walk_times):
        p2.move()
        x, y = p2.get_loc()
        x_list.append(x)
        y_list.append(y)
        distances.append(p2.get_dist())

    print(distances)
    print(x_list)
    print(y_list)


if __name__ == "__main__":
    test()

class Block:

    def __init__(self, conf=None):
        self.conf = {'x': 0, 'y': 0, 'state': True, 'size': 5}
        self.conf.update(conf)

    def __getitem__(self, item):
        return self.conf[item]

    def __setitem__(self, key, value):
        self.conf[key] = value

    def kill(self):
        self.conf['state'] = False


class Player:

    def __init__(self, conf=None):
        self.conf = {'x': 0, 'y': 0, 'width': 20, 'height': 10, 'last_time': 0, 'last_x': 0}
        self.conf.update(conf)

    def __getitem__(self, item):
        return self.conf[item]

    def __setitem__(self, key, value):
        self.conf[key] = value


class Ball:

    def __init__(self, conf=None):
        self.conf = {'x': 0, 'y': 0, 'radius': 3, 'speed': 6,
                     'direction': (0, 0), 'directions':
                         {
                             (0, 0): [0, 4],
                             (1, 0): [1, 5],
                             (2, 0): [1, 4],
                             (3, 0): [2, 4],
                             (4, 0): [2, 3],
                             (5, 0): [3, 3],
                             (6, 0): [3, 2],
                             (7, 0): [4, 2],
                             (8, 0): [4, 1],
                             (9, 0): [5, 1],
                             (-1, 0): [-1, 5],
                             (-2, 0): [-1, 4],
                             (-3, 0): [-2, 4],
                             (-4, 0): [-3, 3],
                             (-5, 0): [-2, 3],
                             (-6, 0): [-3, 2],
                             (-7, 0): [-4, 2],
                             (-8, 0): [-4, 1],
                             (-9, 0): [-5, 1],
                             (0, 1): [0, -4],
                             (1, 1): [1, -5],
                             (2, 1): [1, -4],
                             (3, 1): [2, -4],
                             (4, 1): [2, -3],
                             (5, 1): [3, -3],
                             (6, 1): [3, -2],
                             (7, 1): [4, -2],
                             (8, 1): [4, -1],
                             (9, 1): [5, -1],
                             (-1, 1): [-1, -5],
                             (-2, 1): [-1, -4],
                             (-3, 1): [-2, -4],
                             (-4, 1): [-2, -3],
                             (-5, 1): [-3, -3],
                             (-6, 1): [-3, -2],
                             (-7, 1): [-4, -2],
                             (-8, 1): [-4, -1],
                             (-9, 1): [-5, -1]
                         }}
        self.conf.update(conf)

    def __getitem__(self, item):
        return self.conf[item]

    def __setitem__(self, key, value):
        self.conf[key] = value


class Field:

    def __init__(self, conf=None):
        self.conf = {'height': 100, 'width': 100}
        self.conf.update(conf)

    def __getitem__(self, item):
        return self.conf[item]

    def __setitem__(self, key, value):
        self.conf[key] = value

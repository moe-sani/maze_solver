import copy


def map_to_str(_map):
    map_str = '\n'
    for row in _map:
        for element in row:
            if element == 'X':
                # orange color
                map_str = map_str + ('\33[33m' + 'X' + '\033[0m')
            if element == 'S':
                map_str = map_str + ('\33[32m' + 'S' + '\033[0m')
            if element == 'O':
                # normal color
                map_str = map_str + 'O'
            if element == '*':
                # red color
                map_str = map_str + ('\33[31m' + '*' + '\033[0m')
            if element == 'A':
                # blue color
                map_str = map_str + ('\33[34m' + 'A' + '\033[0m')
        map_str = map_str + '\n'
    return map_str


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    def __eq__(self, other):
        if(self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False

    def __gt__(self, other):
        if(self.x > other.x) and (self.y > other.y):
            return True
        else:
            return False

    def return_right(self):
        p = Point()
        p.x = self.x
        p.y = self.y+1
        return p

    def return_left(self):
        p = Point()
        p.x = self.x
        p.y = self.y-1
        return p

    def return_up(self):
        p = Point()
        p.x = self.x-1
        p.y = self.y
        return p

    def return_down(self):
        p = Point()
        p.x = self.x+1
        p.y = self.y
        return p

    def return_fourside(self):
        p_down = self.return_down()
        p_up = self.return_up()
        p_left = self.return_left()
        p_right = self.return_right()
        lst_foursides = [p_down, p_up, p_right, p_left]
        return lst_foursides


class Map:
    """
    Map class:
    you can print this class directly and will print prettified map
    """
    def __init__(self, map_raw):
        """
        :param map_raw: raw map loaded from a map file
        """
        new_map = []
        for line in map_raw:
            temp = list(line)
            temp.remove('\n')
            new_map.append(temp)
        self.map = new_map
        self.size = self.get_size()
        self.p_start = self.find_start('S')
        self.p_exit = self.find_exit('O')

    def __str__(self):
        return map_to_str(self.map)

    def get_size(self):
        size = Point()
        size.x = len(self.map)
        size.y = len(self.map[0])
        return size

    def value(self, point):
        return self.map[point.x][point.y]

    def find(self, x):
        """
        searches the map to find  x in the map
        :param x:
        :return: x,y location as point
        """
        p = Point()
        for i, row in enumerate(self.map):
            for j, element in enumerate(row):
                if element == x:
                    p.y = j
                    p.x = i
        return p

    def find_start(self, x='S'):
        """
        searches the map to find start position, which is marked by x in the map
        :param x:
        :return: x,y location of the start as a point
        """
        return self.find(x)

    def find_exit(self, x='O'):
        """
        searches 4 borders of the maps to find x, which is considered as exit
        :param x:
        :return: x,y location of the exit as a point
        """
        p = Point()

        for j, item in enumerate(self.map[0]):
            if item == x:
                p.y = j
                p.x = 0

        for j, item in enumerate(self.map[self.size.x-1]):
            if item == x:
                p.y = j
                p.x = self.size.x-1

        for i, item in enumerate(self.map):
            if item[0] == x:
                p.y = 0
                p.x = i

        for i, item in enumerate(self.map):
            if item[self.size.y-1] == x:
                p.y = self.size.y-1
                p.x = i
        return p

    def possible_steps(self, p_current):
        """
        checks surrounding 4 sides of the current point to find 'O'
        :param p_current: current location as a point
        :return: list of points that are found to be 'O'
        """
        lst_foursides = p_current.return_fourside()
        lst_possible = []
        for p_next in lst_foursides:
            if self.size > p_next:
                if self.value(p_next) is 'O':
                    lst_possible.append(p_next)
        return lst_possible


class Path:
    def __init__(self, _map, _p_current=Point(), history=None):
        """
        class of Path
        :param _map: associated map in Map type
        :param history:
        :param _p_current:
        """
        if history is None:
            history = []
        self._map = _map.map
        self._p_current = _p_current
        self.history = copy.deepcopy(history)
        self.successful = False
        self.terminated = False

    def __str__(self):
        temp = []
        for item in self.history:
            temp.append(item.__str__())
        return str(temp)

    @property
    def p_current(self):
        return self._p_current

    @p_current.setter
    def p_current(self, next_point):
        self.history.append(self.p_current)
        self._p_current = next_point

    def get_map_str(self):
        map_new = copy.deepcopy(self._map)
        for point in self.history:
            map_new[point.x][point.y] = '*'
        map_new[self._p_current.x][self._p_current.y] = 'A'
        return map_to_str(map_new)

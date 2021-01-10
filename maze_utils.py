import logging
import copy


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


class Path:
    def __init__(self, p_start=Point()):
        self.p_current = p_start
        self.history = []
        self.finished = False
        self.terminated = False

    def show_history(self):
        temp = []
        for item in self.history:
            temp.append(item.__str__())
        print('---------')
        print('path history:', end='')
        print(temp, end='')
        print(', finished?:', end='')
        print(self.finished, end='')
        print(', terminated?:', end='')
        print(self.terminated)
        print('---------')


class Map:
    def __init__(self, add='map.txt'):
        f = open(add, 'r')
        raw = f.readlines()
        f.close()
        print(raw)
        new_map = []
        for line in raw:
            temp = list(line)
            temp.remove('\n')
            new_map.append(temp)
        self.map = new_map
        self.size = Point()
        self.__size()
        print('new map is loaded successfully!')
        self.show(self.map)
        print('notation is: (x:row,y:column). starting from zero!')
        self.p_start = Point()
        self.p_exit = Point()

    @staticmethod
    def show(mymap):
        map_str = '\nMAP: \n'
        for row in mymap:
            for element in row:
                if element == 'X':
                    map_str = map_str + ('\33[33m' + 'X' + '\033[0m')
                if element == 'S':
                    map_str = map_str + ('\33[32m' + 'S' + '\033[0m')
                if element == 'O':
                    map_str = map_str + 'O'
                if element == '*':
                    map_str = map_str + ('\33[31m' + '*' + '\033[0m')
            map_str = map_str + '\n'
        logging.info(map_str)

    def show_path(self, path):
        print('show_path:')
        map_new = copy.deepcopy(self.map)
        for point in path:
            map_new[point.x][point.y] = '*'
        self.show(map_new)

    def __size(self):
        self.size.x = len(self.map)
        self.size.y = len(self.map[0])
        print('map size is:')
        print(self.size)

    def value(self, point):
        return self.map[point.x][point.y]
    # print('{} is founded in row:{}, and column:{}'.format(x,p.x,p.y))
    # indexes are from zero

    def find(self, x):
        p = Point()
        for i, row in enumerate(self.map):
            for j, element in enumerate(row):
                if element == x:
                    p.y = j
                    p.x = i
        print('{} is found in: ({},{})'.format(x, p.x, p.y))
        self.p_start = p
        return p

    def find_exit(self, x='O'):
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
            # print(item)
            # print(self.size.y-1)
            if item[self.size.y-1] == x:
                p.y = self.size.y-1
                p.x = i
        print('exit is found in: ({},{})'.format(p.x, p.y))
        self.p_exit = p
        return p

    def possible_steps(self, p_current):
        p_down = p_current.return_down()
        p_up = p_current.return_up()
        p_left = p_current.return_left()
        p_right = p_current.return_right()
        lst_foursides = [p_down, p_up, p_right, p_left]
        lst_possible = []
        for p_next in lst_foursides:
            if self.size > p_next:
                if self.value(p_next) is 'O':
                    lst_possible.append(p_next)
        # print('possible steps are:', end='')
        # print_lst(lst_possible)
        return lst_possible

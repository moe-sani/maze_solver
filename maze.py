#!/usr/bin/env python3
"""
maze program
author: Mohammad Fattahi Sani
email: fattahi.m91@gmail.com

"""


import time
import copy
import logging
import argparse
from argparse import RawTextHelpFormatter
from maze_utils import Point, Path, Map


def print_lst(lst):
    temp=[]
    for item in lst:
        temp.append(item.__str__())

    print(temp)
    # print(area(item))


def main(mapfile):
    # load a new map from file
    mymap = Map(mapfile)

    mymap.find('S')
    mymap.find_exit('O')
    init_path = Path(mymap.p_start)
    init_path.history.append(mymap.p_start)
    lst_paths = []
    lst_paths.append(init_path)
    loop_end = False
    counter=0
    while loop_end is False:
        for path in lst_paths:
            # print('new step==========')
            # print('current path:')
            # path.show_history()
            # print('current point in the path')
            # print(path.p_current)
            lst_possible = mymap.possible_steps(path.p_current)
            lst_possible_real = []
            for item in lst_possible:
                # check if we already passed it
                if item not in path.history:
                    lst_possible_real.append(item)

            if len(lst_possible_real) is 0:
                # print('this path is terminated.')
                path.terminated = True

            # print('lst_possible_real')
            # print_lst(lst_possible_real)
            for index, item in enumerate(lst_possible_real):
                if index is 0:
                    # print('next step:')
                    # print(item)
                    path.p_current = item
                    path.history.append(path.p_current)
                else:
                    temp_path = Path()
                    temp_path.history = copy.deepcopy(path.history)
                    temp_path.p_current = item
                    temp_path.history.pop()
                    temp_path.history.append(temp_path.p_current)
                    lst_paths.append(temp_path)
                    # print('new path created!')
                    # print('new path history:')
                    # print_lst(temp_path.history)
            if path.p_current == mymap.p_exit:
                # print('this path is finished!')
                path.finished = True
                path.terminated = True

            time.sleep(0)   # change this to see the steps or debug

        lst_terminated=[]
        for i, found_path in enumerate(lst_paths):
            # print('path number:{}'.format(i))
            # found_path.show_history()
            lst_terminated.append(found_path.terminated)
            if False not in lst_terminated:
                loop_end = True

    lst_finished_paths = []
    lst_path_sizes = []
    mymap.show(mymap.map)
    # print('============ALL Paths are as follows:')
    for found_path in lst_paths:
        # found_path.show_history()
        # print('--------')
        if found_path.finished:
            lst_finished_paths.append(found_path)
    print('============finished Paths are as follows:')
    for index, found_path in enumerate(lst_finished_paths):
        print('path number:{}'.format(index))
        found_path.show_history()
        mymap.show_path(found_path.history)
        lst_path_sizes.append(len(found_path.history))

    print('============shortest path is:')
    min_index = lst_path_sizes.index(min(lst_path_sizes))
    print(min_index)
    mymap.show_path(lst_finished_paths[min_index].history)


# Main function
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Maze Solver',
                                     formatter_class=RawTextHelpFormatter)

    parser.add_argument('--debug', default="INFO", choices={"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"},
                        help="Set the debug level. Standard python levels - ERROR, WARNING, INFO, DEBUG")
    parser.add_argument('--map', default='map.txt',
                        help="provide a map like mymap.txt to solve")

    args = parser.parse_args()

    logging.basicConfig(level=args.debug, format='%(asctime)s - %(threadName)s:%(module)s:%(levelname)s: %(message)s')

    logging.info("Welcome to Maze Solver!")

    main(args.map)

#!/usr/bin/env python3

import time
import copy
import logging
import argparse
from argparse import RawTextHelpFormatter
from maze_utils import Point, Path, Map


def main(mapfile):
    # load a new map from file
    f = open(mapfile, 'r')
    map_raw = f.readlines()
    f.close()
    logging.debug(map_raw)
    mymap = Map(map_raw)
    logging.info('new map is loaded successfully, map size is {}'.format(mymap.size))
    logging.info(mymap)
    logging.debug('notation is: (x:row,y:column). starting from zero!')
    mymap.p_start = mymap.find_start('S')
    mymap.p_exit = mymap.find_exit('O')
    logging.info('map start: {},map exit: {}'.format(mymap.p_start, mymap.p_exit))

    init_path = Path(mymap.p_start)
    lst_paths = [init_path]

    # loop until all the possible paths are terminated
    while False in [path.terminated for path in lst_paths]:
        for path in lst_paths:
            logging.debug('new step==========')
            logging.debug('current path:')
            logging.debug(path)
            logging.debug('current point in the path')
            logging.debug(path.p_current)

            # find all the possible moves
            lst_possible_steps = mymap.possible_steps(path.p_current)
            lst_possible_steps_unseen = []
            for item in lst_possible_steps:
                # check if we already passed it
                if item not in path.history:
                    lst_possible_steps_unseen.append(item)

            if len(lst_possible_steps_unseen) is 0:
                logging.debug('this path is terminated.')
                path.terminated = True
            else:
                logging.debug('lst_possible_real')
                logging.debug(lst_possible_steps_unseen)
                for index, item in enumerate(lst_possible_steps_unseen):
                    if index is 0:
                        logging.debug('next step:')
                        logging.debug(item)
                        path.p_current = item
                    else:
                        # creating new paths is we have more than one possible way to go
                        new_path = Path()
                        new_path.clone(path)
                        new_path.p_current = item
                        lst_paths.append(new_path)
                        logging.debug('new path created!')
            if path.p_current == mymap.p_exit:
                logging.debug('this path is finished!')
                path.finished = True
                path.terminated = True

            time.sleep(0.5)   # change this to see the steps or debug

    lst_finished_paths = []
    lst_path_sizes = []
    logging.info('============ALL Paths are as follows:')
    for found_path in lst_paths:
        logging.info(found_path)
        logging.info('--------')
        if found_path.finished:
            lst_finished_paths.append(found_path)
    logging.info('============finished Paths are as follows:')
    for index, found_path in enumerate(lst_finished_paths):
        logging.info('path number:{}'.format(index))
        logging.debug(found_path)
        logging.debug(found_path.get_map_str(mymap.map))
        lst_path_sizes.append(len(found_path.history))

    logging.info('============shortest path is:')
    min_index = lst_path_sizes.index(min(lst_path_sizes))
    path_shortest = lst_finished_paths[min_index]
    logging.info(path_shortest)
    logging.info(path_shortest.get_map_str(mymap.map))


# Main function
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Maze Solver')

    parser.add_argument('--debug', default="INFO", choices={"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"},
                        help="Set the debug level. Standard python levels - ERROR, WARNING, INFO, DEBUG")
    parser.add_argument('--map', default='map.txt',
                        help="provide a map like mymap.txt to solve")

    args = parser.parse_args()

    logging.basicConfig(level=args.debug, format='> %(levelname)s: %(message)s')

    logging.info("Welcome to Maze Solver!")

    main(args.map)

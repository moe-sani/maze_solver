#!/usr/bin/env python3
import time
import logging
import argparse
from maze_utils import Point, Path, Map


class MazeSolver:
    def __init__(self, mapfile):
        # load a new map from file
        f = open(mapfile, 'r')
        map_raw = f.readlines()
        f.close()
        logging.debug(map_raw)
        self.mymap = Map(map_raw)
        logging.info('New map is loaded successfully, map size is {}'.format(self.mymap.size))
        p_start = self.mymap.find_start('S')
        p_exit = self.mymap.find_exit('O')
        logging.info('Map start: {},map exit: {}'.format(p_start, p_exit))
        logging.debug('Notation is: (x:row,y:column). starting from zero!')
        logging.info(self.mymap)

        self.lst_paths = [Path(self.mymap, p_start)]

    def run(self):
        """
        Loop until all the possible paths are terminated
        Stores the results internally
        :return:
        """
        while False in [path.terminated for path in self.lst_paths]:
            for path in self.lst_paths:
                logging.debug('========== New step ==========')
                logging.debug('Current path: {}'.format(path))
                logging.debug('Current point in the path: {}'.format(path.p_current))
                if path.p_current == self.mymap.p_exit:
                    logging.debug('This path is successful!')
                    path.successful = True
                    path.terminated = True
                else:
                    # Find all the possible moves
                    lst_possible_steps = self.mymap.possible_steps(path.p_current)
                    lst_possible_steps_unseen = []
                    temp = []
                    # Check if we already seen it
                    for step in lst_possible_steps:
                        if step not in path.history:
                            lst_possible_steps_unseen.append(step)
                            temp.append(step.__str__())
                    logging.debug('Possible steps at this point are: {}'.format(temp))

                    if len(lst_possible_steps_unseen) is 0:
                        logging.debug('This path is terminated.')
                        path.terminated = True
                    else:
                        # keep one of the points to assign for the current path. we don't wanna assign it now so that
                        # it wont be copied to new generated paths
                        p_saved = lst_possible_steps_unseen.pop()
                        for step in lst_possible_steps_unseen:
                            # creating new paths as we have more than one possible way to go
                            new_path = Path(self.mymap, path.p_current, path.history)
                            # Assign the remaining points to new paths
                            new_path.p_current = step
                            self.lst_paths.append(new_path)
                            logging.debug('New path has been created for : {}'.format(step))
                        # assign the first point to the current path:
                        path.p_current = p_saved
                        logging.debug('next step: {}'.format(path.p_current))
                time.sleep(0)   # change this to see the steps or debug

    def show_results(self):
        lst_successful_paths = []
        lst_path_sizes = []
        logging.debug('============ ALL Paths are as follows:')
        for found_path in self.lst_paths:
            logging.debug(found_path)
            logging.debug(found_path.get_map_str())
            logging.debug('--------')
            if found_path.successful:
                lst_successful_paths.append(found_path)
        logging.info('============ Successful Paths are as follows:')
        for index, found_path in enumerate(lst_successful_paths):
            logging.info('path number:{}'.format(index))
            logging.info(found_path)
            logging.info(found_path.get_map_str())
            lst_path_sizes.append(len(found_path.history))

        logging.info('============ Shortest path is:')
        min_index = lst_path_sizes.index(min(lst_path_sizes))
        path_shortest = lst_successful_paths[min_index]
        logging.info(path_shortest)
        logging.info(path_shortest.get_map_str())


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

    my_maze_solver = MazeSolver(args.map)
    my_maze_solver.run()
    my_maze_solver.show_results()

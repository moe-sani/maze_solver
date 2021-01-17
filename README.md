# Maze Solver
Maze solver written in Python, to find a shortest route in the given map file

------------------
This code is finding the shortest path for the maze in order to complete the given map.
It requires a map file as an input.
# Features!
  - works for any size of the map, it extracts the map size automatically from the map file.
  - provides prettified command window outputs
  - finds both all paths, and shortest path, and plots them in command window
  - python 3 or higher is required
  - simply improvable to support 3D maps, only by adding third dimension to Point class and a few other changes.
  
You can also:
  - put some delay in sleep() in order to see the steps
  - edit the map file, in any size, and test the code.

### How to run
* clone this repository
* make sure the map file (map.txt) and main file (maze.py) are in the same directory.
* navigate to that directory.
* run the following command
```sh
$ python maze.py
```
you can see the debug outputs by:
```sh
$ python maze.py --debug DEBUG
```
or you can change the map file
```sh
$ python maze.py --map map2.txt
```
## notes:
if new map is not loading
* make sure that the map lines only ends with \n and no other thing. in addition, there should not be any extra lines.
* make sure you have python3

# sample output for the map2 file:

```sh
python maze.py --map map2.txt                                                               [ruby-2.6.3p62]
> INFO: Welcome to Maze Solver!
> INFO: New map is loaded successfully, map size is (7,17)
> INFO: Map start: (4,4),map exit: (1,16)
> INFO:
XXXXXXXXXXXXXXXXX
XOXXOOOXXOOOOOOOO
XOXOOXOXXOXXXXOXX
XOXOXXOOOOOOOOOOX
XOOOSXOXXXXXXXXOX
XXXXXXOOOOOOOOOOX
XXXXXXXXXXXXXXXXX

> INFO: ============ Successful Paths are as follows:
> INFO: path number:0
> INFO: ['(4,4)', '(4,3)', '(3,3)', '(2,3)', '(2,4)', '(1,4)', '(1,5)', '(1,6)', '(2,6)', '(3,6)', '(3,7)', '(3,8)', '(3,9)', '(2,9)', '(1,9)', '(1,10)', '(1,11)', '(1,12)', '(1,13)', '(1,14)', '(1,15)']
> INFO:
XXXXXXXXXXXXXXXXX
XOXX***XX*******A
XOX**X*XX*XXXXOXX
XOX*XX****OOOOOOX
XOO**XOXXXXXXXXOX
XXXXXXOOOOOOOOOOX
XXXXXXXXXXXXXXXXX

> INFO: path number:1
> INFO: ['(4,4)', '(4,3)', '(3,3)', '(2,3)', '(2,4)', '(1,4)', '(1,5)', '(1,6)', '(2,6)', '(3,6)', '(3,7)', '(3,8)', '(3,9)', '(3,10)', '(3,11)', '(3,12)', '(3,13)', '(3,14)', '(2,14)', '(1,14)', '(1,15)']
> INFO:
XXXXXXXXXXXXXXXXX
XOXX***XXOOOOO**A
XOX**X*XXOXXXX*XX
XOX*XX*********OX
XOO**XOXXXXXXXXOX
XXXXXXOOOOOOOOOOX
XXXXXXXXXXXXXXXXX

> INFO: path number:2
> INFO: ['(4,4)', '(4,3)', '(3,3)', '(2,3)', '(2,4)', '(1,4)', '(1,5)', '(1,6)', '(2,6)', '(3,6)', '(4,6)', '(5,6)', '(5,7)', '(5,8)', '(5,9)', '(5,10)', '(5,11)', '(5,12)', '(5,13)', '(5,14)', '(5,15)', '(4,15)', '(3,15)', '(3,14)', '(2,14)', '(1,14)', '(1,15)']
> INFO:
XXXXXXXXXXXXXXXXX
XOXX***XXOOOOO**A
XOX**X*XXOXXXX*XX
XOX*XX*OOOOOOO**X
XOO**X*XXXXXXXX*X
XXXXXX**********X
XXXXXXXXXXXXXXXXX

> INFO: path number:3
> INFO: ['(4,4)', '(4,3)', '(3,3)', '(2,3)', '(2,4)', '(1,4)', '(1,5)', '(1,6)', '(2,6)', '(3,6)', '(4,6)', '(5,6)', '(5,7)', '(5,8)', '(5,9)', '(5,10)', '(5,11)', '(5,12)', '(5,13)', '(5,14)', '(5,15)', '(4,15)', '(3,15)', '(3,14)', '(3,13)', '(3,12)', '(3,11)', '(3,10)', '(3,9)', '(2,9)', '(1,9)', '(1,10)', '(1,11)', '(1,12)', '(1,13)', '(1,14)', '(1,15)']
> INFO:
XXXXXXXXXXXXXXXXX
XOXX***XX*******A
XOX**X*XX*XXXXOXX
XOX*XX*OO*******X
XOO**X*XXXXXXXX*X
XXXXXX**********X
XXXXXXXXXXXXXXXXX

> INFO: ============ Shortest path is:
> INFO: ['(4,4)', '(4,3)', '(3,3)', '(2,3)', '(2,4)', '(1,4)', '(1,5)', '(1,6)', '(2,6)', '(3,6)', '(3,7)', '(3,8)', '(3,9)', '(2,9)', '(1,9)', '(1,10)', '(1,11)', '(1,12)', '(1,13)', '(1,14)', '(1,15)']
> INFO:
XXXXXXXXXXXXXXXXX
XOXX***XX*******A
XOX**X*XX*XXXXOXX
XOX*XX****OOOOOOX
XOO**XOXXXXXXXXOX
XXXXXXOOOOOOOOOOX
XXXXXXXXXXXXXXXXX
```



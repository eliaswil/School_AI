
from enum import Enum
import collections
import random # for filling grid with obstacles
import ue_search as search

# Cell
# Kann nix, ausser S,G,X,*, '' als Inhalt darstellen

class Cell(Enum):
    EMPTY = ' '
    OBSTACLE = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'
    DEBUG = 'D' # only for debugging the labyrinth



# Point as Navigation
    # * y as row
    # * x as column

    # Prototype of Cell location
    # namedtuple needs:
    #  * name
    #  * tuple
Location = collections.namedtuple('Location', 'row column')




# spread_of_obstacles is a value between 0.0 and 1.0
# * * if 0.0 --> there are no obstacles
# * * if 1.0 --> there are no free cells
class Labyrinth:
    
    def __init__(self, rows, cols, spread_of_obstacles, start, goal):
        self.__rows = rows
        self.__cols = cols
        self.__spread_of_obstacles = spread_of_obstacles
        self.__start = start
        self.__goal = goal

        self.__grid = [[Cell.EMPTY for i in range(self.__cols)] for j in range(self.__rows)]

        self._fill_randomly()
        
        self.__grid[self.__start.row][self.__start.column] = Cell.START
        self.__grid[self.__goal.row][self.__goal.column] = Cell.GOAL

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def get_grid(self):
        return self.__grid


    '''
        0 1 2 3 4 5 6 7 8 9 .
       +-+-+-+-+-+-+-+-+-+-+-+-+-+
       | | | | | | | | | | | | | |  row 0
       +-+-+-+-+-+-+-+-+-+-+-+-+-+
       | | |X| | | | | | | | | | |  row 1
       +-+-+-+-+-+-+-+-+-+-+-+-+-+
       | | | | | | | | | | | | | |  ...
       +-+-+-+-+-+-+-+-+-+-+-+-+-+
    '''
    def _fill_randomly(self):
        for row in range(self.__rows):
            for col in range(self.__cols):
                if(random.uniform(0, 1.0) < self.__spread_of_obstacles): # gleichverteilung der Zufallszahlen
                    self.__grid[row][col] = Cell.OBSTACLE
                    pass
                pass
            pass
        pass

    def __str__(self):
        output = ''

        for row in self.__grid:
            output += ''.join(col.value for col in row) + '\n'

        return output
        pass

    '''
    Returns all possible neighbours (r) of a location (o) in the labyrinth. Obstacles are not required.

        0 1 2 3 4 5 6 7 8 9 .
       +-+-+-+-+-+-+-+-+-+-+-+-+-+
       |x| |r| | |x| | | | | | | |  row 0
       +-+-+-+-+-+-+-+-+-+-+-+-+-+
       | |r|o|r| | | | | | | | | |  row 1
       +-+-+-+-+-+-+-+-+-+-+-+-+-+
       |x| |x|x| |x| | | | | | | |  ...
       +-+-+-+-+-+-+-+-+-+-+-+-+-+
    '''
    def get_neighbours(self, location):


        def is_location_blocked(location):
            return self.__grid[location.row][location.column] == Cell.OBSTACLE
        
        def is_location_valid(location, rows, cols):
            return location.column >= 0 and location.column < cols and location.row >= 0 and location.row < rows


        locations = []

        left = Location(location.row, location.column -1)
        right = Location(location.row, location.column + 1)
        top = Location(location.row - 1, location.column)
        bottom = Location(location.row + 1, location.column)

        return [x for x in [left, right, top, bottom] if is_location_valid(x, self.__rows, self.__cols) and not is_location_blocked(x)]
        pass

    def set_path_marker(self, path):
        for location in path:
            self.__grid[location.row][location.column] = Cell.PATH

        self.__grid[self.__start.row][self.__start.column] = Cell.START
        self.__grid[self.__goal.row][self.__goal.column] = Cell.GOAL

    def is_goal(self, location):
        return location == self.__goal

# capturing
def manhatten_distance(goal):

    def distance(location): 
        dist_x = abs(location.column - goal.column)
        dist_y = abs(location.row - goal.row)
        return (dist_x + dist_y)

    return distance # return function distance






def main():
    print(f'name of {Cell.EMPTY.name} and value is {Cell.EMPTY.value}')
    
    start = Location(10, 0)
    goal = Location(0, 8)   

    labyrinth = Labyrinth(11, 11, 0.1, start, goal)
    result = search.depth_first_search(start, labyrinth)

    distance = manhatten_distance(goal)
    result, counter = search.a_star(start, labyrinth, distance)



    print(labyrinth)
    print('-'*50)
    
    if result is not None:
        path = search.generate_path(result)
        labyrinth.set_path_marker(path)

        print(labyrinth)
        print('length: ' + str(len(path)))
    




    pass


if __name__ == '__main__':
    main()
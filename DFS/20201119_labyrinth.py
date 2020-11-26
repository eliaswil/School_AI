
from enum import Enum
import collections

# Cell
# Kann nix, ausser S,G,X,*, '' als Inhalt darstellen

class Cell(Enum):
    EMPTY = '?'
    OBSTACLE = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'



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
        
        self.__grid[self.__start.row][self.__start.column] = Cell.START
        self.__grid[self.__goal.row][self.__goal.column] = Cell.GOAL

    def _fill_randomly(self):
        pass

    def __str__(self):
        output = ''

        for row in self.__grid:
            output += ''.join(col.value for col in row) + '\n'

        return output
        pass






def main():
    print(f'name of {Cell.EMPTY.name} and value is {Cell.EMPTY.value}')
    
    start = Location(10, 0)
    goal = Location(0, 8)

    labyrinth = Labyrinth(11, 11, 0.2, start, goal)
    print(labyrinth)
    
    pass









if __name__ == '__main__':
    main()
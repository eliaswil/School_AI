
from enum import Enum
import collections
import random # for filling grid with obstacles

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


'''
This is the class for the nodes in a graph (stack)
 * Contains a location as state (Zustand)
 * Contains the parent
'''
class Node:
    def __init__(self, state, parent):
        self.__state = state
        self.__parent = parent
        pass

    def __str__(self):
        return '{' + 'state=' + str(self.__state) + ', parent=' + str(self.__parent) + '}'
        pass

class Stack:
    def __init__(self):
        self.__container = [] # list of nodes
        pass
    def __str__(self):
        return '{' + 'container=' + str(self.__container) + '}'

    def pop(self): # return and remove the last element of the stack
        return self.__container.pop()
        pass

    def push(self, node): # add a node to the stack
        self.__container.append(node)
        pass


def main():
    print(f'name of {Cell.EMPTY.name} and value is {Cell.EMPTY.value}')
    
    start = Location(10, 0)
    goal = Location(0, 8)

    labyrinth = Labyrinth(11, 11, 0.1, start, goal)
    print(labyrinth)


    print(labyrinth.get_neighbours(start))
    
    print('-'*50)

    node = Node((1,2), None)
    print(node)

    stack = Stack()
    stack.push(node)

    print(stack)










    pass


if __name__ == '__main__':
    main()
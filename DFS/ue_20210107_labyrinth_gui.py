
import pygame
import sys
import collections

import ue_20210107_search as search
from ue_20210107_labyrinth import Cell, Labyrinth


'''
----------------------------------------------------------------
1. pygame needs to be initialized
2. get a playground
    2.1 set caption
    2.5 get the clock object from pygame
    2.6 set FPS in Loop
3. we have to check some events
4. .....


----------------------------------------------------------------
How GUI works?
 * 25 frames per second
 * each frame will be cleared afterwards new content will be painted
----------------------------------------------------------------


'''

FPS = 60


#2.0
windows_size = (height, width) = (400,400)
playground = pygame.display.set_mode(windows_size)

RED = (255,0,0) # cell color
WHITE = (255,255,255) # border color
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BLACK = (2,2,1)
PINK = (252, 3, 190)

# get the clock for looping
clock = pygame.time.Clock()

#2.1
pygame.display.set_caption('DFS')




def draw_grid(labyrinth):
    cell_size = 20 # 20 pixel

    for y in range(labyrinth.get_rows()):
        for x in range(labyrinth.get_cols()):
            # create a rectangle from pygame - store it in cell
            cell = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)

            color = RED # default (Cell.EMPTY)
            if labyrinth.get_grid()[y][x] == Cell.START:
                color = BLUE

            if labyrinth.get_grid()[y][x] == Cell.GOAL:
                color = GREEN

            if labyrinth.get_grid()[y][x] == Cell.PATH:
                color = WHITE

            if labyrinth.get_grid()[y][x] == Cell.OBSTACLE:
                color = BLACK
    
            pygame.draw.rect(playground, color, cell)
            pygame.draw.rect(playground, BLACK, cell, 1)

    pass



def main():
    pygame.init()

    # BUG
    Location = collections.namedtuple('Location', 'row column')

    start = Location(10, 0)
    goal = Location(0, 8)
    labyrinth = Labyrinth(11, 11, 0.1, start, goal)


    # result = search.depth_first_search(start, labyrinth)
    result = search.breadth_first_search(start, labyrinth)

    # benchmark
    counter = {0: [], 1:[]}
    for i in range(1000):
        result, cntr = search.depth_first_search(start, labyrinth)
        counter[0].append(cntr)
        result, cntr = search.breadth_first_search(start, labyrinth)
        counter[1].append(cntr)
    
    print('-'*50)
    print('DFS: ' + str(sum(counter[0]) / len(counter[0])))
    print('BFS: ' + str(sum(counter[1]) / len(counter[1])))
    
    
    if result is not None:
        path = search.generate_path(result)
        labyrinth.set_path_marker(path)

        print('-'*20 + " Labyrinth " + '-'*20 + '\n')
        print(labyrinth)
        print('-'*50)

    while True:
        # get container of events from pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit')
                pygame.quit() # close windows
                sys.exit() # import sys
            print(event)

        draw_grid(labyrinth)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()




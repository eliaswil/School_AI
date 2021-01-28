from collections import deque
import heapq

class Node:
    def __init__(self, state, parent, cost=0.0, heuristic=0.0):
        self.__state = state
        self.__parent = parent

        # both together are the so called total-cost-cuntion (Gesamtkostenfunktion)
        self.__cost = cost# cost-function
        self.__heuristic = heuristic # distance to goal
        pass

    def __str__(self):
        return '{' + 'state=' + str(self.__state) + ', parent=' + str(self.__parent) + '}'
        pass

    def get_state(self):
        return self.__state

    def get_parent(self):
        return self.__parent

    def get_cost(self):
        return self.__cost

    def get_heuristic(self):
        return self.__heuristic

    def __lt__(self, other_node):
        return (self.__cost + self.__heuristic) < (other_node.get_cost() + other_node.get_heuristic())


'''
This is the class for the nodes in a graph (stack)
 * Contains a location as state (Zustand)
 * Contains the parent
'''
class Stack:
    def __init__(self):
        self.__container = [] # list of nodes
        pass
    def __str__(self):
        return '{' + 'container=' + str(self.__container) + '}'

    def pop(self): # return and remove the last element of the stack
        return self.__container.pop()
        pass

    def empty(self):
        return not self.__container

    def push(self, node): # add a node to the stack
        self.__container.append(node)
        pass


class Queue:
    def __init__(self):
        self.__container = deque()

    def pop(self):
        return self.__container.popleft()

    def push(self, node):
        self.__container.append(node)

    def empty(self):
        return not self.__container

    def __str__(self):
        return '{' + 'container=' + str(self.__container) + '}'


class PriorityQueue:
    def __init__(self):
        self.__container = []
    
    def empty(self):
        return not self.__container

    def pop(self):
        heapq.heappop(self.__container)
        pass

    def push(self, node): 
        heapq.heappush(self.__container, node)
        pass

    def __repr__(self):
        return repr(self.__container)


def depth_first_search(start, grid):
    
    # print('\n' + "="*23 + " DFS " + "="*23 + "\n")

    frontiers = Stack()
    frontiers.push(Node(start, None))

    visited_nodes = {start}
    cntr = 0
    while not frontiers.empty():
        cntr += 1
        current_node = frontiers.pop()
        state = current_node.get_state()

        # termination condition
        if grid.is_goal(state):
            return current_node, cntr

        for neighbour in grid.get_neighbours(state):
            if neighbour in visited_nodes:
                continue

            visited_nodes.add(neighbour)
            frontiers.push(Node(neighbour, current_node))

    return None, cntr

def breadth_first_search(start, grid):
    
    # print('\n' + "="*23 + " BFS " + "="*23 + "\n")

    frontiers = Queue()
    frontiers.push(Node(start, None))

    visited_nodes = {start}
    cntr = 0
    while not frontiers.empty():
        cntr += 1
        current_node = frontiers.pop()
        state = current_node.get_state()

        # termination condition
        if grid.is_goal(state):
            return current_node, cntr

        for neighbour in grid.get_neighbours(state):
            if neighbour in visited_nodes:
                continue

            visited_nodes.add(neighbour)
            frontiers.push(Node(neighbour, current_node))

    return None, cntr



def generate_path(node):
    path = []
    while node.get_parent() is not None:
        node = node.get_parent()
        location = node.get_state()
        path.append(location)

    path.reverse()
    return path

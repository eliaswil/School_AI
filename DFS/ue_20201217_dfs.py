

class Node:
    def __init__(self, state, parent):
        self.__state = state
        self.__parent = parent
        pass

    def __str__(self):
        return '{' + 'state=' + str(self.__state) + ', parent=' + str(self.__parent) + '}'
        pass

    def get_state(self):
        return self.__state

    def get_parent(self):
        return self.__parent

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




def depth_first_search(start, grid):
    
    print('\n' + "="*23 + " DFS " + "="*23 + "\n")

    frontiers = Stack()
    frontiers.push(Node(start, None))

    visited_nodes = {start}

    while not frontiers.empty():
        current_node = frontiers.pop()
        state = current_node.get_state()

        # termination condition
        if grid.is_goal(state):
            return current_node

        for neighbour in grid.get_neighbours(state):
            if neighbour in visited_nodes:
                continue

            visited_nodes.add(neighbour)
            frontiers.push(Node(neighbour, current_node))

    return None

def generate_path(node):
    path = []
    while node.get_parent() is not None:
        node = node.get_parent()
        location = node.get_state()
        path.append(location)

    path.reverse()
    return path

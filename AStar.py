import Maze

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    start_point = Node(None, start) #[x,y]
    start_point.g = start_point.h = strart_point.f = 0
    end_point = Node(None, end) #[x,y]
    end_point.g = end_point.h = end_point.f = 0
    open = []
    closed = []
    open.append(start_point)
    
    while len(open) > 0:
        current_point = open[0]
        current_index = 0
        for index, item in enumerate(open):
            if item.f < current_point.f:
                current_point = item
                current_index = index
        
        open.pop(current_index)
        closed.append(current_point)

        if current_point == end_point:
            path = []
            current = current_point
            while current in not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        
        children = []
        for new_position in [(0,-1), (1,0), (0,1), (-1,0)]:
            point_position = (current_point.position[0] + new_position[0], current_point.position[1] + new_position[1])
            if point_position[0] > (len(maze) - 1) or point_position[0] < 0 or point_position[1] > (len(maze[len(maze) - 1]) - 1) or point_position[1] < 0:
                continue
            if maze[point_position[0]][point_position[1]] != 0:
                continue
            new_point = Node(current_point, point_position)
            children.append(new_point)

        for child in children:
            for closed_child in closed:
                if child == closed_child:
                    continue
            
            child.g = current_point.g + 1
            child.h = abs(child[0] - start_point[0]) + abs(child[1] - start_point[1])
            child.f = child.g + child.h

            for point in open:
                if child == point and child.g > point.g:
                    continue
            open.append(child)

def main():
    

from PIL import Image
import numpy as np

class Maze:
    def __init__(self):
        self.maze = Image.open('Maze_1.jpg', 'r')
        self.width, self.height = self.maze.size
    
    def create_pixel_map(self):
        array = np.array(self.maze, dtype=np.uint8)
        self.pixel_map = Image.fromarray(array)
        return array


maze = Maze()
print(maze.create_pixel_map())
#print(maze.map)
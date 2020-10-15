from PIL import Image


class Maze:
    def __init__(self):
        self.maze = Image.open('Maze_1.jpg', 'r')
        self.width, self.height = self.maze.size
    
    def create_pixel_map(self):
        self.pixel_map = []
        lst = []
        for n, pixel in enumerate(self.maze.getdata()):
            if n % self.width == 0:
               self.pixel_map.append(lst)
               lst = []
            if pixel[0] > 125:
                lst.append(0)
            else:
                lst.append(1)
        return self.pixel_map


#m = Maze()
#print(m.create_pixel_map())
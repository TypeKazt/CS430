import numpy as np
from colors import Color


class XpmGenerator(object):
    def __init__(self, height, width, colors=set(), shapes=[]):
        self.height = height
        self.width = width
        self.grid = np.full((height, width), Color.white(), dtype=Color)
        self.colors = colors | set([s.color for s in shapes] + [Color.white()])
        self.shapes = []
        for i in shapes:
            self.add_shape(i)
        self.xpm_doc = ""

    def add_shape(self, shape):
        self.shapes.append(shape)
        self.add_color(shape.color)
        shape.raster(self.grid)

    def add_color(self, color):
        self.colors.add(color)

    def generate_xpm(self):
        result = "/*XPM*/\nstatic char *sco100[] = {\n\
                /* width height num_colors chars_per_pixel */\n"
        result += '"%d %d %d %d",\n' % (self.width, self.height,
                                        len(self.colors),
                                        max(len(c.id) for c in self.colors))

        result += "/* colors */\n"
        for c in self.colors:
            result += '"' + c.id + " c #" + c.to_hex()[2:] + '",\n'

        result += "/*pixels*/\n"
        for row in range(len(self.grid)):
            result += '"'
            for p in self.grid[row]:
                result += p.id
            result += '",\n'
        result += '"'
        for p in self.grid[-1]:
            result += p.id
        result += '"\n};'

        self.xpm_doc = result
        return result

from colors import *


class Shape(object):
    """Parent Shape object"""
    def __init__(self):
        self.color = Color()
        self.width = 1
        self.max_x = 1
        self.max_y = 1

    def get_coor(self):
        pass

    def set_coor(self):
        pass

    def _set_max_coor(self):
        pass

    def raster(self, np_grid):
        pass


class Line(Shape):
    """Line Object"""
    def __init__(self, x_1, y_1, x_2, y_2):
        super(Line, self).__init__()
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.slope = (float(y_2-y_2) / float(x_2-x_2))

    def __str__(self):
        return "Line: %d %d %d %d" % (self.x_1, self.y_1, self.x_2, self.y_2)

    def _set_max_coor(self):
        self.max_x = self.x_2
        self.max_y = self.y_2

    def get_coor(self):
        """get_coor() -> List 
        List containing coordinates [x1, y1, x2, y2]"""

        return [self.x_1, self.y_1, self.x_2, self.y_2]

    def set_coor(self, x_1, y_1, x_2, y_2):
        self.x_1, self.y_1, self.x_2, self.y_2 = \
                x_1, y_1, x_2, y_2
    
    def raster(self, np_grid):
        pass

    def dda(self, np_grid):
        pass

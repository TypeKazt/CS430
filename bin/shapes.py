from colors import *
from numpy import inf


class Shape(object):
    """Parent Shape object"""
    def __init__(self):
        self.color = Black()
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
        self.slope = 0
        if x_2 == x_1:
            self.slope = inf
        else:
            self.slope = (float(y_2-y_1) / float(x_2-x_1))

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
    
    def raster(self, np_grid, algo=0):
        if algo == 0:
            self._dda(np_grid)
        else:
            pass

    def _dda(self, np_grid):
        if self.slope < 1 and self.slope >= 0:
            self._dda_pos_x(np_grid)
        elif self.slope > 1:
            self._dda_pos_y(np_grid)
        elif self.slope < 0 and self.slope >= -1:
            self._dda_neg_x(np_grid)
        else:
            self._dda_neg_y(np_grid)

    def _dda_pos_x(self, np_grid):
        y_pos = self.y_1
        for i in range(self.x_1, self.x_2):
            if self.slope*(i-self.x_1)-(y_pos-self.y_1) >= 0.5:
                y_pos += 1
            np_grid[len(np_grid)-1-y_pos][i] = self.color

    def _dda_pos_y(self, np_grid):
        x_pos = self.x_1
        for i in range(self.y_1, self.y_2):
            if (i-self.y_1)/self.slope - (x_pos-self.x_1) >= 0.5:
                x_pos += 1
            np_grid[len(np_grid)-1-i][x_pos] = self.color

    def _dda_neg_x(self, np_grid):
        y_pos = self.y_1
        for i in range(self.x_1, self.x_2):
            if self.slope*(i-self.x_1)+(y_pos-self.y_1) <= -0.5:
                y_pos += 1
            np_grid[len(np_grid)-1-(2*self.y_1-y_pos)][i] = self.color

    def _dda_neg_y(self, np_grid):
        x_pos = self.x_1
        for i in range(self.y_1-self.y_2):
            if i/self.slope + (x_pos-self.x_1) <= -0.5:
                x_pos += 1
            np_grid[len(np_grid)-1-(self.y_1-i)][x_pos] = self.color


    



from colors import *
from numpy import inf


class Point2D(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def coor(self):
        return [self.x, self.y]

    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return True
        return False

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.x != other.x:
            return self.x > other.x
        return self.y > other.y

    def __lt__(self, other):
        return not self > other        

    def __sub__(self, other):
        return Vector2D(self.x-other.x,
                        self.y-other.y)

    def __add__(self, other):
        return Point2D(self.x+other.x,
                       self.y+other.y)

    def __str__(self):
        return "%d %d" % (self.x, self.y)

    def __mul__(self, other):
        if type(other) == Point2D:
            return self.x*other.x + self.y*other.y
        elif type(other) == Vector2D:
            return Vector2D(other.x*self.x,
                            other.y*self.y)


class Vector2D(Point2D):
    def normals(self):
        vec1 = Vector2D(self.y, -self.x)
        vec2 = Vector2D(-self.y, self.x)
        return [vec1, vec2]

    def __mul__(self, other):
        if type(other) == Vector2D:
            return self.x*other.x + self.y*other.y
        elif type(other) == Point2D:
            return Vector2D(other.x*self.x,
                            other.y*self.y)
        return Vector2D(self.x*other, self.y*other)


class Shape(object):
    """Parent Shape object"""
    def __init__(self):
        self.color = Black()
        self.width = 1
        self.max_x = 1
        self.max_y = 1
        self.rasterable = True

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
        self.p1 = Point2D(x_1, y_1)
        self.p2 = Point2D(x_2, y_2)
        self.slope = 0
        if x_2 == x_1:
            self.slope = inf
        else:
            self.slope = (float(y_2-y_1) / float(x_2-x_1))

    def __str__(self):
        return "P1:" + str(self.p1) + " P2:" + str(self.p2)

    def _set_max_coor(self):
        self.max_x = self.x_2
        self.max_y = self.y_2

    def get_coor(self):
        """get_coor() -> List 
        List containing coordinates [x1, y1, x2, y2]"""

        return [self.p1, self.p2]

    def set_coor(self, x_1, y_1, x_2, y_2):
        self.x_1, self.y_1, self.x_2, self.y_2 = \
                x_1, y_1, x_2, y_2
    
    def raster(self, np_grid, algo=0):

        self._cohen_sutherland(len(np_grid), len(np_grid[0]))
        if self.rasterable:
            self._dda(np_grid)

    def _dda(self, np_grid):
        if self.slope <= 1 and self.slope >= 0:
            self._dda_pos_x(np_grid)
        elif self.slope > 1:
            self._dda_pos_y(np_grid)
        elif self.slope < 0 and self.slope >= -1:
            self._dda_neg_x(np_grid)
        else:
            self._dda_neg_y(np_grid)

    def _dda_pos_x(self, np_grid):
        y_pos = self.p1.y
        for i in range(self.p1.x, self.p2.x):
            if self.slope*(i-self.p1.x)-(y_pos-self.p1.y) >= 0.5:
                y_pos += 1
            np_grid[len(np_grid)-1-y_pos][i] = self.color

    def _dda_pos_y(self, np_grid):
        x_pos = self.p1.x
        for i in range(self.p1.y, self.p2.y):
            if (i-self.p1.y)/self.slope - (x_pos-self.p1.x) >= 0.5:
                x_pos += 1
            np_grid[len(np_grid)-1-i][x_pos] = self.color

    def _dda_neg_x(self, np_grid):
        y_pos = self.p1.y
        for i in range(self.p1.x, self.p2.x):
            if self.slope*(i-self.p1.x)+(y_pos-self.p1.y) <= -0.5:
                y_pos += 1
            np_grid[len(np_grid)-1-(2*self.p1.y-y_pos)][i] = self.color

    def _dda_neg_y(self, np_grid):
        x_pos = self.p1.x
        for i in range(self.p1.y-self.p2.y):
            if i/self.slope + (x_pos-self.p1.x) <= -0.5:
                x_pos += 1
            np_grid[len(np_grid)-1-(self.p1.y-i)][x_pos] = self.color

    def _compute_bounds_code(self, height, width):
        inside, left, right, bottom, top = \
        0, 1, 2, 4, 8

        start_code = inside
        end_code = inside

        if self.p1.x < 0:
            start_code |= left
        elif self.p1.x >= width:
            start_code |= right
        if self.p1.y < 0:
            start_code |= bottom
        elif self.p1.y >= height:
            start_code |= top

        if self.p2.x < 0:
            end_code |= left
        elif self.p2.x >= width:
            end_code |= right
        if self.p2.y < 0:
            end_code |= bottom
        elif self.p2.y >= height:
            end_code |= top

        return [start_code, end_code]

    def _cohen_sutherland(self, height, width):
        start_code, end_code = self._compute_bounds_code(height, width)
        self.rasterable = False
        inside, left, right, bottom, top = \
        0, 1, 2, 4, 8

        while(True):
            if((start_code | end_code) == 0):
                self.rasterable = True
                break
            elif ((start_code & end_code) != 0):
                break
            else:
                x, y = 0, 0
                outcode = start_code or end_code

                if outcode & top:
                    x = self.p1.x + (self.p2.x - self.p1.x) * \
                            (height - 1 - self.p1.y) / (self.p2.y - self.p1.y)
                    y = height-1
                elif outcode & bottom:
                    x = self.p1.x + (self.p2.x - self.p1.x) * \
                            (0 - self.p1.y) / (self.p2.y - self.p1.y)
                    y = 0
                elif outcode & right:
                    y = self.p1.y + (self.p2.y - self.p1.y) * \
                            (width - 1 - self.p1.x) / (self.p2.x - self.p1.x)
                    x = width-1
                elif outcode & left:
                    y = self.p1.y + (self.p2.y - self.p1.y) * \
                            (0 - self.p1.x) / (self.p2.x - self.p1.x)
                    x = 0
                else:
                    raise Exception("Undefined clipping state")

                if outcode == start_code:
                    self.p1.x = int(round(x))
                    self.p1.y = int(round(y))
                    start_code = self._compute_bounds_code(height, width)[0]
                else:
                    self.p2.x = int(round(x))
                    self.p2.y = int(round(y))
                    end_code = self._compute_bounds_code(height, width)[1]

    def parametric_line(self, t):
        return self.p1 + (self.p2-self.p1)*t
        
    def _cyrus_beck(self, width, height):
        D = self.p2 - self.p1
        Nl, Nt, Nr, Nb = Vector2D(-1, 0), Vector2D(0, 1), \
            Vector2D(1, 0), Vector2D(0, -1)

        max_le = 0
        for Ni in [Nl, Nb]:
            P_type = Ni*D
            t = 0
            if P_type != 0:
                t = (Ni*(self.p1-Point2D(0, 0)))/-P_type
            if t > max_le:
                max_le = t

        min_te = 1
        for Ni in [Nt, Nr]:
            P_type = Ni*D
            t = 1
            if P_type != 0:
                t = (Ni*(self.p1-Point2D(width, height*Ni.y)))/-(Ni*D)
            if t < min_te:
                min_te = t

        if max_le > min_te:
            self.rasterable = False

        self.p1 = self.parametric_line(max_le)
        self.p2 = self.parametric_line(min_te)

        self.p1 = Point2D(int(round(self.p1.x)), int(round(self.p1.y)))
        self.p2 = Point2D(int(round(self.p2.x)), int(round(self.p2.y)))


class Polygon(Shape):
    def __init__(self, start_point=None):
        super(Polygon, self).__init__()
        self.start_point = start_point
        self.line_stack = []
        self.point_stack = []
        if start_point is not None:
            self.point_stack = [start_point]

    def add_line(self, line):
        self.line_stack.append(line)

    def add_point(self, point):
        self.point_stack.append(point)

    def _sutherland_hodgman(self, clipPolygon):
        def inside(point):
            return(cp2.x-cp1.x)*(point.y-cp1.y) > (cp2.y-cp1.y)*(point.x-cp1.x)

        def compute_intersection():
            dc = [cp1.x - cp2.x, cp1.y - cp2.y]
            dp = [s.x - e.x, s.y - e.y]
            n1 = cp1.x * cp2.y - cp1.y * cp2.x
            n2 = s.x * e.y - s.y * e.x
            n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
            return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]

        out_points = self.point_stack
        cp1 = clipPolygon.point_stack[-1]

        for c_vertex in clipPolygon.point_stack[1:]:
            cp2 = c_vertex
            in_points = out_points
            out_points = []
            if in_points == []:
                self.point_stack = []
                break
            s = in_points[-1]
            for s_vertex in in_points:
                e = s_vertex
                if inside(e):
                    if not inside(s):
                        out_points.append(Point2D(*compute_intersection()))
                    out_points.append(e)
                elif inside(s):
                    out_points.append(Point2D(*compute_intersection()))
                s = e
            cp1 = cp2

        self.point_stack = out_points

    def raster(self, np_grid):
        frame_buffer_poly = Polygon(Point2D(0, 0))
        frame_buffer_poly.add_point(Point2D(500, 0))
        frame_buffer_poly.add_point(Point2D(500, 500))
        frame_buffer_poly.add_point(Point2D(0, 500))
        frame_buffer_poly.add_point(Point2D(0, 0))
        self._sutherland_hodgman(frame_buffer_poly)
        line_stack = []
        for i in range(len(self.point_stack)-1):
            p1 = self.point_stack[0+i]
            p2 = self.point_stack[1+i]
            line_stack.append(Line(*min(p1, p2).coor()+max(p1, p2).coor()))
        for line in line_stack:
            line.raster(np_grid)

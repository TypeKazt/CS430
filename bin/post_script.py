from shapes import *
from colors import *


class PsParser(object):
    def __init__(self, filename=None):
        self.filename = filename
        # The functions dict is responsible for all custom shape functions
        # Allows new shapes to be added without modifying main parser
        self.functions = {
                "Line": self._generate_line,
                "moveto": self._push_polygon,
                "lineto": self._add_poly_point,
                "stroke": self._poly_stroke
                }
        self.polygon_stack = []

    def _poly_stroke(self, data):
        return self.polygon_stack.pop()

    def _add_poly_point(self, data):
        my_poly = self.polygon_stack[-1]
        int_data = [int(i) for i in data]
        my_poly.add_point(Point2D(*int_data))

    def _push_polygon(self, data):
        poly = Polygon(Point2D(int(data[0]), int(data[1])))
        self.polygon_stack.append(poly)

    def _generate_line(self, data):
        """_generate_line(data) -> Line

        Private"""

        massaged_data = [int(i) for i in data]
        start = massaged_data[:2]
        end = massaged_data[2:]
        massaged_data = min(start, end)+max(start, end)
        return Line(*massaged_data)

    def parse_file(self):
        """parse_file() -> list 
        -- Parses a PS file and returns list of Shapes"""

        object_list = []
        with open(self.filename, "r") as f:
            start = False
            for line in f:
                if "%" == line[0]:
                    start = not start
                elif start:
                    data = line.split()
                    if data != []:
                        shape = self.functions[data[-1]](data[:-1])
                        if shape is not None:
                            object_list.append(shape)
        return object_list



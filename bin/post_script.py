from shapes import *
from colors import *


class PsParser(object):
    def __init__(self, filename=None):
        self.filename = filename
        # The functions dict is responsible for all custom shape functions
        # Allows new shapes to be added without modifying main parser
        self.functions = {
                "Line": self._generate_line
                }

    def _generate_line(self, data):
        """_generate_line(data) -> Line

        Private"""
        return Line(*[int(i) for i in data[:-1]])

    def parse_file(self):
        """parse_file() -> list 
        -- Parses a PS file and returns list of Shapes"""

        object_list = []
        with open(self.filename) as f:
            start = False
            for line in f:
                if "%" == line[0]:
                    start = not start
                elif start:
                    data = line.split()
                    object_list.append(self.functions[data[-1]](data))
        return object_list



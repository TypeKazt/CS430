from space_points import Point3D


class SMFParser(object):
    def __init__(self, filename=None):
        self.filename = filename
        self.functions = {
                "v": self._generate_vertex,
                "f": self._generate_polygon
                }
        self.vertices = []
        self.polygons = []
   
    def _generate_vertex(self, data):
        self.vertices.append(Point3D(*[float(i) for i in data]))

    def _generate_polygon(self, data):
        pass

    def parse(self):
        with open(self.filename, 'r') as f:
            for line in f:
                data = line.split(" ")
                self.functions[data[0]](data[1:])

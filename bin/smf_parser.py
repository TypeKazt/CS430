from space_points import Point3D, Face3D


class SMFParser(object):
    def __init__(self, filename=None):
        self.filename = filename
        self.functions = {
                "v": self._generate_vertex,
                "f": self._generate_face
                }
        self.vertices = []
        self.faces = []
   
    def _generate_vertex(self, data):
        self.vertices.append(Point3D(*[float(i) for i in data]))

    def _generate_face(self, data):
        self.faces.append(Face3D([self.vertices[int(i)-1] for i in data]))

    def parse(self):
        with open(self.filename, 'r') as f:
            for line in f:
                data = line.split(" ")
                self.functions[data[0]](data[1:])
        return [self.vertices, self.faces]

class Point2D(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.hcoor = 1

    def coor(self):
        return [self.x, self.y, self.hcoor]

    def set_coor(self, x, y, hcoor):
        self.x, self.y, self.hcoor = x, y, hcoor

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


class Point3D(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.hcoor = 1

    def coor(self):
        return [self.x, self.y, self.z, self.hcoor]

    def set_coor(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                if self.z == other.z:
                    return True
        return False

    '''def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.x != other.x:
            return self.x > other.x
        if self.y != ot

    def __lt__(self, other):
        return not self > other'''

    def __sub__(self, other):
        return Vector3D(self.x-other.x,
                        self.y-other.y,
                        self.z-other.z)

    def __add__(self, other):
        return Point3D(self.x+other.x,
                       self.y+other.y,
                       self.z+other.z)

    def __str__(self):
        return "%d %d %d" % (self.x, self.y, self.z)

    def __mul__(self, other):
        if type(other) == Point2D:
            return self.x*other.x + self.y*other.y + self.z*other.z
        elif type(other) == Vector3D:
            return Vector2D(other.x*self.x,
                            other.y*self.y,
                            other.z*self.z)


class Vector3D(Point3D):
    def __mul__(self, other):
        if type(other) == Vector3D:
            return self.x*other.x + self.y*other.y + self.z*other.z
        elif type(other) == Point3D:
            return Vector3D(other.x*self.x,
                            other.y*self.y,
                            other.z*self.z)
        return Vector3D(self.x*other, self.y*other, self.z*other.z)

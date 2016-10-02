class Color(object):
    def __init__(self, r=0, g=0, b=0):
        assert r in range(256) and g in range(256) and b in range(256)
        self.red = r
        self.green = g
        self.blue = b
        self.id = ""
        self.rgb = [self.red, self.green, self.blue]

    def __hash__(self):
        return hash(self.id)

    def to_hex(self):
        """to_hex() -> String -- 6 char hex string of color"""

        result = "0x"
        for i in self.rgb:
            temp = hex(i)[2:]
            if i < 16:
                result += "0"
            result += temp
        return result

    @staticmethod
    def black():
        return Black()

    @staticmethod
    def white():
        return White()


class Black(Color):
    def __init__(self):
        super(Black, self).__init__()
        self.id = "x"


class White(Color):
    def __init__(self):
        super(White, self).__init__()
        self.id = "-"
        self.red = 255
        self.green = 255
        self.blue = 255
        self.rgb = [self.red, self.green, self.blue]


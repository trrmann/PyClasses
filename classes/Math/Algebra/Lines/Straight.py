# Straight.py

import Line
from Geometry import Shape

class StraightLineError(Line.LineError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Straight(Line("Straight", "0 dimension", "Straight", ["x", "y"])):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, x={self.x}, y={self.y})"

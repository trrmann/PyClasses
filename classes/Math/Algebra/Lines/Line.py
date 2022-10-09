# Line.py

import Algebra
from Geometry import Shape

class LineError(Shape.ShapeError, Algebra.AlgebraError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Line(Shape("Line", "0 dimension", "Line", ["x", "y"]), Algebra("Line")):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, x={self.x}, y={self.y})"

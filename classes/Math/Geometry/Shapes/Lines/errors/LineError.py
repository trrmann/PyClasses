# LineError.py
from Classes.Math.Algebra.Lines.errors.LineError import LineError as AlgebraLineError
from Classes.Math.Geometry.Shapes.errors.ShapeError import ShapeError

class LineError(ShapeError, AlgebraLineError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

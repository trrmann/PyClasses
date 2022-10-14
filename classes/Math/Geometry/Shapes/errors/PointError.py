# PointError.py
from Classes.Math.Geometry.Shapes.errors.ShapeError import ShapeError
from Classes.Math.Algebra.Coordinates.errors.PointError import PointError as AlgebraPointError

class PointError(AlgebraPointError, ShapeError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

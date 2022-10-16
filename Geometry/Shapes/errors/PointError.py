# PointError.py
import Classes.Math.Geometry.Shapes.errors.ShapeError as ShapeError
import Classes.Math.Algebra.Coordinates.errors.PointError as AlgebraPointError

class PointError(AlgebraPointError.PointError, ShapeError.ShapeError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

# PythagorianError.py
import Classes.Math.Geometry.Shapes.Triangles.errors.RightTriangleError as RightTriangleError

class PythagorianError(RightTriangleError.RightTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

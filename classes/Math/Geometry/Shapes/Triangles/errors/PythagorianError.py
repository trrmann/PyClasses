# PythagorianError.py
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError

class PythagorianError(TriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

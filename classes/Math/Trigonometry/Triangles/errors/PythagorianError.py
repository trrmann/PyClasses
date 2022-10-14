# PythagorianError.py
import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.errors.PythagorianError import PythagorianError as GeometryPythagorianError

class PythagorianError(TriangleError, GeometryPythagorianError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

# ScaleneTriangleError.py
from Classes.Math.Trigonometry.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.errors.ScaleneTriangleError import ScaleneTriangleError as GeometryScaleneTriangleError

class ScaleneTriangleError(TriangleError, GeometryScaleneTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

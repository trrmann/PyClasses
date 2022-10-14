# Right.py
from Classes.Math.Trigonometry.Triangles.errors.ScaleneTriangleError import ScaleneTriangleError
from Classes.Math.Geometry.Shapes.Triangles.errors.RightTriangleError import RightTriangleError as GeometryRightTriangleError

class RightTriangleError(ScaleneTriangleError, GeometryRightTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

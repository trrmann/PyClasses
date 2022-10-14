# IsoscelesTriangleError.py
from Classes.Math.Trigonometry.Triangles.errors.ScaleneTriangleError import ScaleneTriangleError
from Classes.Math.Geometry.Shapes.Triangles.errors.IsoscelesTriangleError import IsoscelesTriangleError as GeometryIsoscelesTriangleError

class IsoscelesTriangleError(ScaleneTriangleError, GeometryIsoscelesTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

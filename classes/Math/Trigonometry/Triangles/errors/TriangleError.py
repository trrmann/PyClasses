# TriangleError.py
from Classes.Math.Trigonometry.errors.TrigonometryError import TrigonometryError
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError as GeometryTriangleError

class TriangleError(TrigonometryError, GeometryTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

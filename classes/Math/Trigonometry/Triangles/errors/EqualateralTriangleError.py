# Equalateral.py
from Classes.Math.Trigonometry.Triangles.errors.IsoscelesTriangleError import IsoscelesTriangleError
from Classes.Math.Geometry.Shapes.Triangles.errors.EqualateralTriangleError import EqualateralTriangleError as GeometryEqualateralTriangleError

class EqualateralTriangleError(IsoscelesTriangleError, GeometryEqualateralTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

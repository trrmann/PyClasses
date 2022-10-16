# Equalateral.py
import Classes.Math.Trigonometry.Triangles.errors.IsoscelesTriangleError as IsoscelesTriangleError
import Classes.Math.Geometry.Shapes.Triangles.errors.EqualateralTriangleError as GeometryEqualateralTriangleError

class EqualateralTriangleError(IsoscelesTriangleError.IsoscelesTriangleError, GeometryEqualateralTriangleError.EqualateralTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

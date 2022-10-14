# Equalateral.py
from Classes.Math.Trigonometry.Triangles.Isosceles import IsoscelesTriangle
from Classes.Math.Geometry.Shapes.Triangles.Equalateral import EqualateralTriangle as GeometryEqualateralTriangle

class EqualateralTriangle(IsoscelesTriangle, GeometryEqualateralTriangle):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "EqualateralTriangle"):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", "EqualateralTriangle", ["a", "b", "c"])

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

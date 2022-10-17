# Equalateral.py
import Classes.Math.Trigonometry.Triangles.Isosceles as IsoscelesTriangle
import Classes.Math.Geometry.Shapes.Triangles.Equalateral as GeometryEqualateralTriangle

class EqualateralTriangle(IsoscelesTriangle.IsoscelesTriangle, GeometryEqualateralTriangle.EqualateralTriangle):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "EqualateralTriangle"):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", "EqualateralTriangle", ["a", "b", "c"])

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

# Isosceles.py
from Classes.Math.Geometry.Shapes.Triangles.Scalene import ScaleneTriangle, ScaleneTriangleError

class IsoscelesTriangleError(ScaleneTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class IsoscelesTriangle(ScaleneTriangle):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "IsoscelesTriangle"):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", "IsoscelesTriangle", ["a", "b", "c"])

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

# Scalene.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle, TriangleError

class ScaleneTriangleError(TriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class ScaleneTriangle(Triangle):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "ScaleneTriangle"):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", "ScaleneTriangle", ["a", "b", "c"])

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

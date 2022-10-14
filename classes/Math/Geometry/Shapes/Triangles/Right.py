# Right.py
from Classes.Math.Geometry.Shapes.Triangles.Scalene import ScaleneTriangle
from Classes.Math.Geometry.errors.MissingDimensionError import MissingDimensionError

class RightTriangle(ScaleneTriangle):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "RightTriangle"):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", "RightTriangle", ["a", "b", "c"])

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

    def A(self):
        return A_right_triangle(self.a, self.b)

def A_right_triangle(base, height):
    try:
        return float(base) * float(height) / 2
    except ValueError:
        try:
            float(base)
            raise MissingDimensionError(f"Missing the height dimension for the triangle!", "triangle", "height")
        except ValueError:
            raise MissingDimensionError(f"Missing the length of the base dimension for the triangle!", "triangle", "base")

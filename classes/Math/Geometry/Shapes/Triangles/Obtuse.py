# Obtuse.py
import Classes.Math.Geometry.Shapes.Triangles.Scalene as ScaleneTriangle

class ObtuseTriangle(ScaleneTriangle.ScaleneTriangle):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "ObtuseTriangle"):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", "ObtuseTriangle", ["a", "b", "c"])

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

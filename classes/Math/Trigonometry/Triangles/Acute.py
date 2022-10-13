# Acute.py
from Classes.Math.Trigonometry.Triangles.Scalene import ScaleneTriangle, ScaleneTriangleError
from Classes.Math.Geometry.Shapes.Triangles.Acute import AcuteTriangle as GeometryAcuteTriangle,  AcuteTriangleError as GeometryAcuteTriangleError

class AcuteTriangleError(ScaleneTriangleError, GeometryAcuteTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class AcuteTriangle(ScaleneTriangle, GeometryAcuteTriangle):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "AcuteTriangle"):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", "AcuteTriangle", ["a", "b", "c"])

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

# AcuteTriangleError.py
from Classes.Math.Trigonometry.Triangles.errors.ScaleneTriangleError import ScaleneTriangleError
from Classes.Math.Geometry.Shapes.Triangles.errors.AcuteTriangleError import AcuteTriangleError as GeometryAcuteTriangleError

class AcuteTriangleError(ScaleneTriangleError, GeometryAcuteTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

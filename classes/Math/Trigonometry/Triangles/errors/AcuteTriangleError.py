# AcuteTriangleError.py
import Classes.Math.Trigonometry.Triangles.errors.ScaleneTriangleError as ScaleneTriangleError
import Classes.Math.Geometry.Shapes.Triangles.errors.AcuteTriangleError as GeometryAcuteTriangleError

class AcuteTriangleError(ScaleneTriangleError.ScaleneTriangleError, GeometryAcuteTriangleError.AcuteTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

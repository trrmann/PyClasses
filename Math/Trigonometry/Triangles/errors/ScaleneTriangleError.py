# ScaleneTriangleError.py
import Classes.Math.Trigonometry.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.errors.ScaleneTriangleError as GeometryScaleneTriangleError

class ScaleneTriangleError(TriangleError.TriangleError, GeometryScaleneTriangleError.ScaleneTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

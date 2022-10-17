# Right.py
import Classes.Math.Trigonometry.Triangles.errors.ScaleneTriangleError as ScaleneTriangleError
import Classes.Math.Geometry.Shapes.Triangles.errors.RightTriangleError as GeometryRightTriangleError

class RightTriangleError(ScaleneTriangleError.ScaleneTriangleError, GeometryRightTriangleError.RightTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

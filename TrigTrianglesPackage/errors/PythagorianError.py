# PythagorianError.py
import Classes.Math.Geometry.Shapes.Triangles.errors.PythagorianError as GeometryPythagorianError
import Classes.Math.Trigonometry.Triangles.errors.TriangleError as TriangleError

class PythagorianError(TriangleError.TriangleError, GeometryPythagorianError.PythagorianError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

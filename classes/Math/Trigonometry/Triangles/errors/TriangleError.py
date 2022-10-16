# TriangleError.py
import Classes.Math.Trigonometry.errors.TrigonometryError as TrigonometryError
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as GeometryTriangleError

class TriangleError(TrigonometryError.TrigonometryError, GeometryTriangleError.TriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

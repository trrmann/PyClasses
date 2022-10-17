# TriangleError.py
from ShapesPackage.ShapeErrorModule import ShapeError
from TrigonometryPackage.TrigonometryErrorModule import TrigonometryError

class TriangleError(ShapeError, TrigonometryError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

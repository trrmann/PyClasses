# PointError.py
from ShapesPackage.ClosedShapeErrorModule import ClosedShapeError
from ShapesPackage.PointModule import Point
from CoordinatesPackage.CoordinatesErrorModule import CoordinatesError

class PointError(ClosedShapeError, CoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Point=Point()):
        super().__init__(str(msg), classes)
        self.classes = classes

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"
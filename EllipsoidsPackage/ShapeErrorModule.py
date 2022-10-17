# Shape.py
from GeometryPackage.GeometryErrorModule import GeometryError
from ShapesPackage.ShapeModule import Shape

class ShapeError(GeometryError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Shape=Shape()):
        super().__init__(str(msg), classes)
        self.classes = classes

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"
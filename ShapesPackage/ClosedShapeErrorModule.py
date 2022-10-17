# ClosedShapeErrorModule.py
from ShapesPackage.ClosedShapeModule import ClosedShape
from ShapesPackage.OpenShapeErrorModule import OpenShapeError
from ShapesPackage.ShapeModule import Shape

class ClosedShapeError(OpenShapeError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: ClosedShape=ClosedShape()):
        super().__init__(str(msg), classes)
        self.classes = classes

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"
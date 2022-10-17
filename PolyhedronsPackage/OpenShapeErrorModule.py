# OpenShapeErrorModule.py
from ShapesPackage.OpenShapeModule import OpenShape
from ShapesPackage.ShapeErrorModule import ShapeError
from ShapesPackage.ShapeModule import Shape

class OpenShapeError(ShapeError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: OpenShape=OpenShape()):
        super().__init__(str(msg), classes)
        self.classes = classes

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"
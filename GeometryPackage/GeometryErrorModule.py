# GeometryError.py
from AlgebraPackage.AlgebraErrorModule import AlgebraError
from GeometryPackage.GeometryModule import Geometry

class GeometryError(AlgebraError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Geometry=Geometry()):
        super().__init__(str(msg), classes)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"
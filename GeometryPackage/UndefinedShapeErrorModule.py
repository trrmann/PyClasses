# UndefinedShapeError.py
from GeometryPackage.GeometryErrorModule import GeometryError
from GeometryPackage.GeometryModule import Geometry

class UndefinedShapeError(GeometryError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg:  str, classObject:  Geometry=Geometry(), shapeName:  str="Undefined"):
        super.__init__(classObject, msg)
        self.shapeName = shapeName

    def __repr__(self) -> str:
        return f"{type(self).__name__} (classes:({self.classes}), shape:({self.shapeName}), msg=\"{self.msg}\")"
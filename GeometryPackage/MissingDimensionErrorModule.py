# Geometry.py
from GeometryPackage.GeometryErrorModule import GeometryError
from GeometryPackage.GeometryModule import Geometry

class MissingDimensionError(GeometryError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg:  str, classObject:  Geometry=Geometry(), shapeName:  str="Undefined", dimensionName:  str="Undefined"):
        super.__init__(classObject, msg)
        self.shapeName = shapeName
        self.dimensionName = dimensionName

    def __repr__(self) -> str:
        return f"{type(self).__name__} (classes:({self.classes}), shape:({self.shapeName}), dimension:({self.dimensionName}), msg=\"{self.msg}\")"
# Shape.py
from GeometryPackage.GeometryModule import Geometry

class Shape(Geometry):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, classification, type, dimensions, className = "Shape"):
        super().__init__(className)
        self.classification = classification
        self.type = type
        self.dimensions = dimensions

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions})"

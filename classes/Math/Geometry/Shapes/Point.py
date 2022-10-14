# Point.py
from Classes.Math.Geometry.Shapes.Shape import Shape
from Classes.Math.Algebra.Coordinates.Point import Point as AlgebraPoint

class Point(AlgebraPoint, Shape):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, coordinates, className = "Point", classification="0 dimension", type="Point", dimensions=["coordinates"]):
        super().__init__(self, className = className)
        super().__init__(self, classification, type, dimensions, className = className)
        self.coordinates = coordinates

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, coordinates={self.coordinates})"

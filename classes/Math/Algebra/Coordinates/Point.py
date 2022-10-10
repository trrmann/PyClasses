# Point.py
from Classes.Math.Algebra.Coordinates.Coordinates import Coordinates, CoordinatesError
#from Classes.Math.Geometry.Shapes.Shape import Shape, ShapeError

#class PointError(CoordinatesError, ShapeError):
class PointError(CoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

#class Point(Coordinates, Shape):
class Point(Coordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

#    def __init__(self, coordinates, className = "Point", classification="0 dimension", type="Point", dimensions=["coordinates"]):
#        super().__init__(self, className = className)
#        super().__init__(self, classification, type, dimensions, className = className)
#        self.coordinates = coordinates
    def __init__(self,
            coordinates,
            className = "Point"
        ):
        super().__init__(self, className = className)
        self.coordinates = coordinates

#    def __repr__(self) -> str:
#        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, coordinates={self.coordinates})"
    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinates={self.coordinates})"

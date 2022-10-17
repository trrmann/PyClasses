# PolygonModule.py
from CoordinatesPackage.CoordinatesModule import Coordinates
from EllipsesPackage.ShapeModule import Shape
from GridsPackage.GridModule import Grid
from CartesianGridPackage.CartesianGridCoordinatesModule import CartesianGridCoordinates

class Polygon(Shape):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            grid: Grid = CartesianGridCoordinates(),
            coordinates:  Coordinates = "undefined",
            dimensions = "undefined",
            classification: str = "2 dimensions",
            type: str = "Polygon",
            className: str = "Polygon"
        ):
        super().__init__(
            className = className,
            grid = grid,
            coordinates = coordinates,
            dimensions = dimensions,
            start = "self",
            classification = classification,
            type = type,
            className= className
        )


    def __init__(self,
            grid: Grid = CartesianGridCoordinates(),
            coordinates:  Coordinates = "undefined",
            dimensions = "undefined",
            classification: str = "unclassified",
            type: str = "undefined",
            className: str = "Shape"
        ):
        super().__init__(className)
        self.grid = grid
        self.coordinates = coordinates
        self.dimensions = dimensions
        self.classification = classification
        self.type = type

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, grid={self.grid}, coordinates={self.coordinates}, dimensions={self.dimensions})"

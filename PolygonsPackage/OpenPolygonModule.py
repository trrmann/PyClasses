# OpenShapeModule.py
from CoordinatesPackage.CoordinatesModule import Coordinates
from GridsPackage.GridModule import Grid
from CartesianGridPackage.CartesianGridCoordinatesModule import CartesianGridCoordinates
from ShapesPackage.ShapeModule import Shape

class OpenShape(Shape):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            grid: Grid = CartesianGridCoordinates(),
            coordinates:  Coordinates = "undefined",
            dimensions = "undefined",
            start = "undefined",
            end = "undefined",
            classification: str = "0 dimensions",
            type: str = "Point",
            className: str = "Point"
        ):
        super().__init__(
            className = className,
            grid = grid,
            coordinates = coordinates,
            dimensions = dimensions,
            classification = classification,
            type = type,
            className= className
        )
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, grid={self.grid}, coordinates={self.coordinates}, dimensions={self.dimensions}, start={self.start}, end={self.end})"
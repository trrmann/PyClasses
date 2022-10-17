# ClosedShapeModule.py
from CoordinatesPackage.CoordinatesModule import Coordinates
from GridsPackage.GridModule import Grid
from CartesianGridPackage.CartesianGridCoordinatesModule import CartesianGridCoordinates
from ShapesPackage.OpenShapeModule import OpenShape

class ClosedShape(OpenShape):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


    def __init__(self,
            grid: Grid = CartesianGridCoordinates(),
            coordinates:  Coordinates = "undefined",
            dimensions = "undefined",
            start = "undefined",
            classification: str = "0 dimensions",
            type: str = "Point",
            className: str = "Point"
        ):
        super().__init__(
            className = className,
            grid = grid,
            coordinates = coordinates,
            dimensions = dimensions,
            start = start,
            end = start,
            classification = classification,
            type = type,
            className= className
        )

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, grid={self.grid}, coordinates={self.coordinates}, dimensions={self.dimensions}, start={self.start}, end={self.end})"
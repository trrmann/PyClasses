# ThreeDCartesianGridCoordinatesError.py
from Classes.Math.Algebra.Coordinates.Grids.Cartesian.errors.TwoDCartesianGridCoordinatesError import TwoDCartesianGridCoordinatesError
from Classes.Math.Algebra.Coordinates.errors.ThreeDCoordinatesError import ThreeDCoordinatesError

class ThreeDCartesianGridCoordinatesError(TwoDCartesianGridCoordinatesError, ThreeDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

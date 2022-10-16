# ThreeDCartesianGridCoordinatesError.py
import Classes.Math.Algebra.Coordinates.Grids.Cartesian.errors.TwoDCartesianGridCoordinatesError as TwoDCartesianGridCoordinatesError
import Classes.Math.Algebra.Coordinates.errors.ThreeDCoordinatesError as ThreeDCoordinatesError

class ThreeDCartesianGridCoordinatesError(TwoDCartesianGridCoordinatesError.TwoDCartesianGridCoordinatesError, ThreeDCoordinatesError.ThreeDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

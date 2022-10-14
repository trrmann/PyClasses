# ThreeDCylindricalGridCoordinatesError.py
from Classes.Math.Algebra.Coordinates.Grids.Cylindrical.errors.TwoDCylindricalGridCoordinatesError import TwoDCylindricalGridCoordinatesError
from Classes.Math.Algebra.Coordinates.errors.ThreeDCoordinatesError import ThreeDCoordinatesError

class ThreeDCylindricalGridCoordinatesError(TwoDCylindricalGridCoordinatesError, ThreeDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

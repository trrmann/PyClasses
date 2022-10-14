# TwoDCylindricalGridCoordinatesError.py
from Classes.Math.Algebra.Coordinates.Grids.Cylindrical.errors.CylindricalGridCoordinatesError import CylindricalGridCoordinatesError
from Classes.Math.Algebra.Coordinates.errors.TwoDCoordinatesError import TwoDCoordinatesError

class TwoDCylindricalGridCoordinatesError(CylindricalGridCoordinatesError, TwoDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

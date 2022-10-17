# TwoDCylindricalGridCoordinatesError.py
from CoordinatesPackage.TwoDCoordinatesErrorModule import TwoDCoordinatesError
from CylindricalGridPackage.CylindricalGridCoordinatesErrorModule import CylindricalGridCoordinatesError

class TwoDCylindricalGridCoordinatesError(CylindricalGridCoordinatesError, TwoDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

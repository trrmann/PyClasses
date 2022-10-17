# ThreeDCylindricalGridCoordinatesError.py
from CoordinatesPackage.ThreeDCoordinatesErrorModule import ThreeDCoordinatesError
from CylindricalGridPackage.TwoDCylindricalGridCoordinatesErrorModule import TwoDCylindricalGridCoordinatesError

class ThreeDCylindricalGridCoordinatesError(TwoDCylindricalGridCoordinatesError, ThreeDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

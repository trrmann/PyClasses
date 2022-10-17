# ThreeDPolarGridCoordinatesError.py
from CoordinatesPackage.ThreeDCoordinatesErrorModule import ThreeDCoordinatesError
from PolarGridPackage.TwoDPolarGridCoordinatesErrorModule import TwoDPolarGridCoordinatesError

class ThreeDPolarGridCoordinatesError(TwoDPolarGridCoordinatesError, ThreeDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

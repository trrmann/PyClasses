# FourDCartesianGridCoordinatesError.py
from CartesianGridPackage.ThreeDCartesianGridCoordinatesErrorModule import ThreeDCartesianGridCoordinatesError
from CoordinatesPackage.FourDCoordinatesErrorModule import FourDCoordinatesError

class FourDCartesianGridCoordinatesError(ThreeDCartesianGridCoordinatesError, FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

# FourDCylindricalGridCoordinatesError.py
from CoordinatesPackage.FourDCoordinatesErrorModule import FourDCoordinatesError
from CylindricalGridPackage.ThreeDCylindricalGridCoordinatesErrorModule import ThreeDCylindricalGridCoordinatesError

class FourDCylindricalGridCoordinatesError(ThreeDCylindricalGridCoordinatesError, FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

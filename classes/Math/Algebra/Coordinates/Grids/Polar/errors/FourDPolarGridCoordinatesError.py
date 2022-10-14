# FourDPolarGridCoordinatesError.py
from Classes.Math.Algebra.Coordinates.Grids.Polar.errors.ThreeDPolarGridCoordinatesError import ThreeDPolarGridCoordinatesError
from Classes.Math.Algebra.Coordinates.errors.FourDCoordinatesError import FourDCoordinatesError

class FourDPolarGridCoordinatesError(ThreeDPolarGridCoordinatesError, FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

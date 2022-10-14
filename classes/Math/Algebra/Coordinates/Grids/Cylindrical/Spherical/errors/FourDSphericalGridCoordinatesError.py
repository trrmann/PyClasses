# FourDSphericalGridCoordinatesError.py
from Classes.Math.Algebra.Coordinates.Grids.Cylindrical.Spherical.errors.ThreeDSphericalGridCoordinatesError import ThreeDSphericalGridCoordinatesError
from Classes.Math.Algebra.Coordinates.errors.FourDCoordinatesError import FourDCoordinatesError

class FourDSphericalGridCoordinatesError(ThreeDSphericalGridCoordinatesError, FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

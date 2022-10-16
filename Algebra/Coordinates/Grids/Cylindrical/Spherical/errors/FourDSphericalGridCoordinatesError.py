# FourDSphericalGridCoordinatesError.py
import Classes.Math.Algebra.Coordinates.Grids.Cylindrical.Spherical.errors.ThreeDSphericalGridCoordinatesError as ThreeDSphericalGridCoordinatesError
import Classes.Math.Algebra.Coordinates.errors.FourDCoordinatesError as FourDCoordinatesError

class FourDSphericalGridCoordinatesError(ThreeDSphericalGridCoordinatesError.ThreeDSphericalGridCoordinatesError, FourDCoordinatesError.FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

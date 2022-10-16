# ThreeDSphericalGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Cylindrical.Spherical.errors.SphericalGridCoordinatesError as SphericalGridCoordinatesError
import Classes.Math.Algebra.Coordinates.errors.ThreeDCoordinatesError as ThreeDCoordinatesError

class ThreeDSphericalGridCoordinatesError(SphericalGridCoordinatesError.SphericalGridCoordinatesError, ThreeDCoordinatesError.ThreeDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

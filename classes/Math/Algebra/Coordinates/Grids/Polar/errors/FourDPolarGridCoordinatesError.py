# FourDPolarGridCoordinatesError.py
import Classes.Math.Algebra.Coordinates.Grids.Polar.errors.ThreeDPolarGridCoordinatesError as ThreeDPolarGridCoordinatesError
import Classes.Math.Algebra.Coordinates.errors.FourDCoordinatesError as FourDCoordinatesError

class FourDPolarGridCoordinatesError(ThreeDPolarGridCoordinatesError.ThreeDPolarGridCoordinatesError, FourDCoordinatesError.FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

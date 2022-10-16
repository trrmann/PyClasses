# FourDHomogeneousGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Homogeneous.errors.ThreeDHomogeneousGridCoordinatesError as ThreeDHomogeneousGridCoordinatesError
import Classes.Math.Algebra.Coordinates.errors.FourDCoordinatesError as FourDCoordinatesError

class FourDHomogeneousGridCoordinatesError(ThreeDHomogeneousGridCoordinatesError.ThreeDHomogeneousGridCoordinatesError, FourDCoordinatesError.FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

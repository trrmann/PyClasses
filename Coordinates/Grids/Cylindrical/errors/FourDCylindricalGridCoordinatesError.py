# FourDCylindricalGridCoordinatesError.py
import Classes.Math.Algebra.Coordinates.Grids.Cylindrical.errors.ThreeDCylindricalGridCoordinatesError as ThreeDCylindricalGridCoordinatesError
import Classes.Math.Algebra.Coordinates.errors.FourDCoordinatesError as FourDCoordinatesError

class FourDCylindricalGridCoordinatesError(ThreeDCylindricalGridCoordinatesError.ThreeDCylindricalGridCoordinatesError, FourDCoordinatesError.FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

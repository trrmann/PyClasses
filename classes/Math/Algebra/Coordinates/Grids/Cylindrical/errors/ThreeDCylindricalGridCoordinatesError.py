# ThreeDCylindricalGridCoordinatesError.py
import Classes.Math.Algebra.Coordinates.Grids.Cylindrical.errors.TwoDCylindricalGridCoordinatesError as TwoDCylindricalGridCoordinatesError
import Classes.Math.Algebra.Coordinates.errors.ThreeDCoordinatesError as ThreeDCoordinatesError

class ThreeDCylindricalGridCoordinatesError(TwoDCylindricalGridCoordinatesError.TwoDCylindricalGridCoordinatesError, ThreeDCoordinatesError.ThreeDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

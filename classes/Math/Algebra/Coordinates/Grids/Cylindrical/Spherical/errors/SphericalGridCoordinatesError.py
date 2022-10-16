# SphericalGridCoordinatesError.py
import Classes.Math.Algebra.Coordinates.Grids.Cylindrical.errors.CylindricalGridCoordinatesError as CylindricalGridCoordinatesError

class SphericalGridCoordinatesError(CylindricalGridCoordinatesError.CylindricalGridCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

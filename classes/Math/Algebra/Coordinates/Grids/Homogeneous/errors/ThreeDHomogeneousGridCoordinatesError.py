# ThreeDHomogeneousGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Homogeneous.errors.HomogeneousGridCoordinatesError import HomogeneousGridCoordinatesError
from Classes.Math.Algebra.Coordinates.errors.ThreeDCoordinatesError import ThreeDCoordinatesError

class ThreeDHomogeneousGridCoordinatesError(HomogeneousGridCoordinatesError, ThreeDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

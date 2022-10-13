# PolarGridCoordinatesError.py
from Classes.Math.Algebra.Coordinates.Grids.errors.GridError import GridError

class PolarGridCoordinatesError(GridError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

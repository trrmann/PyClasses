# TwoDPolarGridCoordinatesError.py
import Classes.Math.Algebra.Coordinates.Grids.Polar.errors.PolarGridCoordinatesError as PolarGridCoordinatesError
import Classes.Math.Algebra.Coordinates.errors.TwoDCoordinatesError as TwoDCoordinatesError

class TwoDPolarGridCoordinatesError(PolarGridCoordinatesError.PolarGridCoordinatesError, TwoDCoordinatesError.TwoDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

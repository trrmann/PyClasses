# TwoDPolarGridCoordinatesError.py
import PolarGridCoordinatesError
from Classes.Math.Algebra.Coordinates.errors.TwoDCoordinatesError import TwoDCoordinatesError

class TwoDPolarGridCoordinatesError(PolarGridCoordinatesError, TwoDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

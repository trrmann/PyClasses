# TwoDCoordinatesError.py
import Classes.Math.Algebra.Coordinates.errors.CoordinatesError as CoordinatesError

class TwoDCoordinatesError(CoordinatesError.CoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

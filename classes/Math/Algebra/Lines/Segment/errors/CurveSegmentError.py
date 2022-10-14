# CurveSegmentError.py
import LineSegmentError
from Classes.Math.Algebra.Lines.errors.CurveError import CurveError

class CurveSegmentError(CurveError, LineSegmentError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

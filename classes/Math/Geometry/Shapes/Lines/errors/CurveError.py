# Curve.py
from Classes.Math.Geometry.Shapes.Lines.errors.LineError import LineError
from Classes.Math.Algebra.Lines.errors.CurveError import CurveError as AlgebraCurveError

class CurveError(LineError, AlgebraCurveError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

# Curve.py
from Classes.Math.Geometry.Shapes.Lines.Line import Line, LineError
from Classes.Math.Algebra.Lines.Curve import Curve as AlgebraCurve, CurveError as AlgebraCurveError

class CurveError(LineError, AlgebraCurveError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Curve(Line, AlgebraCurve):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList,
            className = "Curve"
        ):
        super().__init__(self, coordinatesList = coordinatesList, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList})"

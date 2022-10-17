# ArcError.py
import Classes.Math.Geometry.Shapes.Lines.errors.LineError as LineError
import Classes.Math.Algebra.Lines.errors.ArcError as AlgebraArcError

class ArcError(LineError.LineError, AlgebraArcError.ArcError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

# CurveError.py
import Classes.Math.Algebra.Lines.errors.LineError as LineError

class CurveError(LineError.LineError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

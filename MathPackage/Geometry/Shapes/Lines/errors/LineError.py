# LineError.py
import Classes.Math.Algebra.Lines.errors.LineError as AlgebraLineError
import Classes.Math.Geometry.Shapes.errors.ShapeError as ShapeError

class LineError(ShapeError.ShapeError, AlgebraLineError.LineError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

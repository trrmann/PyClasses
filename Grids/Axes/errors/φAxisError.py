# φAxisError.py
import Classes.Math.Algebra.Coordinates.Grids.Axes.errors.AxisError as AxisError

class φAxisError(AxisError.AxisError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

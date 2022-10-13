# TwoDPolorGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Polar.PolarGridCoordinates import PolorGridCoordinates, PolorGridCoordinatesError
from Classes.Math.Algebra.Coordinates.Grids.Axes.ρAxis import ρAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis import θAxis
from Classes.Math.Algebra.Coordinates.TwoDCoordinates import TwoDCoordinates, TwoDCoordinatesError

class TwoDPolorGridCoordinatesError(PolorGridCoordinatesError, TwoDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class TwoDPolorGridCoordinates(PolorGridCoordinates, TwoDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [ρAxis, θAxis],
            className = "TwoDPolorGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"
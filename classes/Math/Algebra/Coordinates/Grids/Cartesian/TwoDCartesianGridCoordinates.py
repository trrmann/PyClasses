# TwoDCartesianGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Cartesian.CartesianGridCoordinates import CartesianGridCoordinates
from Classes.Math.Algebra.Coordinates.TwoDCoordinates import TwoDCoordinates
from Classes.Math.Algebra.Coordinates.Grids.Axes.XAxis import XAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.YAxis import YAxis

class TwoDCartesianGridCoordinates(CartesianGridCoordinates, TwoDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [XAxis, YAxis],
            className = "TwoDCartesianGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

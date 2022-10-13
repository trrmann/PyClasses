# ThreeDCartesianGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Cartesian.TwoDCartesianGridCoordinates import TwoDCartesianGridCoordinates
from Classes.Math.Algebra.Coordinates.Grids.Axes.XAxis import XAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.YAxis import YAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.ZAxis import ZAxis
from Classes.Math.Algebra.Coordinates.ThreeDCoordinates import ThreeDCoordinates

class ThreeDCartesianGridCoordinates(TwoDCartesianGridCoordinates, ThreeDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [XAxis, YAxis, ZAxis],
            className = "ThreeDCartesianGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

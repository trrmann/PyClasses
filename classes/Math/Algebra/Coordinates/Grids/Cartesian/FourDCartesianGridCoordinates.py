# FourDCartesianGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Cartesian.ThreeDCartesianGridCoordinates import ThreeDCartesianGridCoordinates, ThreeDCartesianGridCoordinatesError
from Classes.Math.Algebra.Coordinates.Grids.Axes.XAxis import XAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.YAxis import YAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.ZAxis import ZAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.TimeLine import TimeLine
from Classes.Math.Algebra.Coordinates.FourDCoordinates import FourDCoordinates, FourDCoordinatesError

class FourDCartesianGridCoordinates(ThreeDCartesianGridCoordinatesError, FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class FourDCartesianGridCoordinates(ThreeDCartesianGridCoordinates, FourDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [XAxis, YAxis, ZAxis, TimeLine],
            className = "FourDCartesianGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

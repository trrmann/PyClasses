# FourDCartesianGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Cartesian.ThreeDCartesianGridCoordinates as ThreeDCartesianGridCoordinates
import Classes.Math.Algebra.Coordinates.Grids.Axes.XAxis as XAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.YAxis as YAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.ZAxis as ZAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.TimeLine as TimeLine
import Classes.Math.Algebra.Coordinates.FourDCoordinates as FourDCoordinates

class FourDCartesianGridCoordinates(ThreeDCartesianGridCoordinates.ThreeDCartesianGridCoordinates, FourDCoordinates.FourDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [XAxis.XAxis, YAxis.YAxis, ZAxis.ZAxis, TimeLine.TimeLine],
            className = "FourDCartesianGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

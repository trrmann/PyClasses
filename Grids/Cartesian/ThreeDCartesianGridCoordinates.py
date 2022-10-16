# ThreeDCartesianGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Cartesian.TwoDCartesianGridCoordinates as TwoDCartesianGridCoordinates
import Classes.Math.Algebra.Coordinates.Grids.Axes.XAxis as XAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.YAxis as YAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.ZAxis as ZAxis
import Classes.Math.Algebra.Coordinates.ThreeDCoordinates as ThreeDCoordinates

class ThreeDCartesianGridCoordinates(TwoDCartesianGridCoordinates.TwoDCartesianGridCoordinates, ThreeDCoordinates.ThreeDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [XAxis.XAxis, YAxis.YAxis, ZAxis.ZAxis],
            className = "ThreeDCartesianGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

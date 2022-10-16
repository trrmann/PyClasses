# TwoDCartesianGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Cartesian.CartesianGridCoordinates as CartesianGridCoordinates
import Classes.Math.Algebra.Coordinates.TwoDCoordinates as TwoDCoordinates
import Classes.Math.Algebra.Coordinates.Grids.Axes.XAxis as XAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.YAxis as YAxis

class TwoDCartesianGridCoordinates(CartesianGridCoordinates.CartesianGridCoordinates, TwoDCoordinates.TwoDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [XAxis.XAxis, YAxis.YAxis],
            className = "TwoDCartesianGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

# TwoDPolorGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Polar.PolarGridCoordinates as PolorGridCoordinates
import Classes.Math.Algebra.Coordinates.Grids.Axes.ρAxis as ρAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis as θAxis
import Classes.Math.Algebra.Coordinates.TwoDCoordinates as TwoDCoordinates

class TwoDPolorGridCoordinates(PolorGridCoordinates.PolorGridCoordinates, TwoDCoordinates.TwoDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [ρAxis.ρAxis, θAxis.θAxis],
            className = "TwoDPolorGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

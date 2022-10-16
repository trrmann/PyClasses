# TwoDCylindricalGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Cylindrical.CylindricalGridCoordinates as CylindricalGridCoordinates
import Classes.Math.Algebra.Coordinates.TwoDCoordinates as TwoDCoordinates
import Classes.Math.Algebra.Coordinates.Grids.Axes.rAxis as rAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis as θAxis

class TwoDCylindricalGridCoordinates(CylindricalGridCoordinates.CylindricalGridCoordinates, TwoDCoordinates.TwoDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [rAxis.rAxis, θAxis.θAxis],
            className = "TwoDCylindricalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

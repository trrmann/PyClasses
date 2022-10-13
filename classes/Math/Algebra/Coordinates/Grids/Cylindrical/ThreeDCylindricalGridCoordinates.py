# ThreeDCylindricalGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Cylindrical.TwoDCylindricalGridCoordinates import TwoDCylindricalGridCoordinates
from Classes.Math.Algebra.Coordinates.Grids.Axes.rAxis import rAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis import θAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.ZAxis import ZAxis
from Classes.Math.Algebra.Coordinates.ThreeDCoordinates import ThreeDCoordinates

class ThreeDCylindricalGridCoordinates(TwoDCylindricalGridCoordinates, ThreeDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [rAxis, θAxis, ZAxis],
            className = "ThreeDCylindricalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

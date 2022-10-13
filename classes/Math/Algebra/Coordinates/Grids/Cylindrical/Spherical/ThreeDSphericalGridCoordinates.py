# ThreeDSphericalGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Cylindrical.Spherical.SphericalGridCoordinates import SphericalGridCoordinates
from Classes.Math.Algebra.Coordinates.Grids.Axes.ρAxis import ρAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis import θAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.φAxis import φAxis
from Classes.Math.Algebra.Coordinates.ThreeDCoordinates import ThreeDCoordinates

class ThreeDSphericalGridCoordinates(SphericalGridCoordinates, ThreeDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [ρAxis, θAxis, φAxis],
            className = "ThreeDSphericalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

# FourDSphericalGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Cylindrical.Spherical.ThreeDSphericalGridCoordinates import ThreeDSphericalGridCoordinates
from Classes.Math.Algebra.Coordinates.Grids.Axes.ρAxis import ρAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis import θAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.φAxis import φAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.TimeLine import TimeLine
from Classes.Math.Algebra.Coordinates.FourDCoordinates import FourDCoordinates

class FourDSphericalGridCoordinates(ThreeDSphericalGridCoordinates, FourDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [ρAxis, θAxis, φAxis, TimeLine],
            className = "FourDSphericalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

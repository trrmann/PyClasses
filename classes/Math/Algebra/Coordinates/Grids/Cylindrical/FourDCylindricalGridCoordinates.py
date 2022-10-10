# FourDCylindricalGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Cylindrical.ThreeDCylindricalGridCoordinates import ThreeDCylindricalGridCoordinates, ThreeDCylindricalGridCoordinatesError
from Classes.Math.Algebra.Coordinates.Grids.Axes.rAxis import rAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis import θAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.ZAxis import ZAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.TimeLine import TimeLine
from Classes.Math.Algebra.Coordinates.FourDCoordinates import FourDCoordinates, FourDCoordinatesError

class FourDCylindricalGridCoordinatesError(ThreeDCylindricalGridCoordinatesError, FourDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class FourDCylindricalGridCoordinates(ThreeDCylindricalGridCoordinates, FourDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [rAxis, θAxis, ZAxis, TimeLine],
            className = "FourDCylindricalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

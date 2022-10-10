# TwoDCylindricalGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Cylindrical.CylindricalGridCoordinates import CylindricalGridCoordinates, CylindricalGridCoordinatesError
from Classes.Math.Algebra.Coordinates.TwoDCoordinates import TwoDCoordinates, TwoDCoordinatesError
from Classes.Math.Algebra.Coordinates.Grids.Axes.rAxis import rAxis
from Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis import θAxis

class TwoDCylindricalGridCoordinatesError(CylindricalGridCoordinatesError, TwoDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class TwoDCylindricalGridCoordinates(CylindricalGridCoordinates, TwoDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [rAxis, θAxis],
            className = "TwoDCylindricalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

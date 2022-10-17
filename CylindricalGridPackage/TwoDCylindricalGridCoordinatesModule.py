# TwoDCylindricalGridCoordinates.py
from AxesPackage.rAxisModule import rAxis
from AxesPackage.θAxisModule import θAxis
from CoordinatesPackage.TwoDCoordinatesModule import TwoDCoordinates
from CylindricalGridPackage.CylindricalGridCoordinatesModule import CylindricalGridCoordinates

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

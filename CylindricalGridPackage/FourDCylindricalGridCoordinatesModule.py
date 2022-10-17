# FourDCylindricalGridCoordinates.py
from AxesPackage.TimeLineModule import TimeLine
from AxesPackage.ZAxisModule import ZAxis
from AxesPackage.rAxisModule import rAxis
from AxesPackage.θAxisModule import θAxis
from CoordinatesPackage.FourDCoordinatesModule import FourDCoordinates
from CylindricalGridPackage.ThreeDCylindricalGridCoordinatesModule import ThreeDCylindricalGridCoordinates

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

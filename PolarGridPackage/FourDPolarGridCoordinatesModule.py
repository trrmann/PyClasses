# FourDPolarGridCoordinates.py
from AxesPackage.TimeLineModule import TimeLine
from AxesPackage.θAxisModule import θAxis
from AxesPackage.ρAxisModule import ρAxis
from AxesPackage.φAxisModule import φAxis
from CoordinatesPackage.FourDCoordinatesModule import FourDCoordinates
from PolarGridPackage.ThreeDPolarGridCoordinatesModule import ThreeDPolarGridCoordinates

class FourDPolarGridCoordinates(ThreeDPolarGridCoordinates, FourDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [ρAxis, θAxis, φAxis, TimeLine],
            className = "FourDPolarGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

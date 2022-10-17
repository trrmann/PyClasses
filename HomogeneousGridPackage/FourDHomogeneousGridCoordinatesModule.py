# FourDHomogeneousGridCoordinates.py
from AxesPackage.TimeLineModule import TimeLine
from AxesPackage.XAxisModule import XAxis
from AxesPackage.YAxisModule import YAxis
from AxesPackage.ZAxisModule import ZAxis
from CoordinatesPackage.FourDCoordinatesModule import FourDCoordinates
from HomogeneousGridPackage.ThreeDHomogeneousGridCoordinatesModule import ThreeDHomogeneousGridCoordinates

class FourDHomogeneousGridCoordinates(ThreeDHomogeneousGridCoordinates, FourDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [XAxis, YAxis, ZAxis, TimeLine],
            className = "FourDHomogeneousGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

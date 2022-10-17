# ThreeDHomogeneousGridCoordinates.py
from AxesPackage.XAxisModule import XAxis
from AxesPackage.YAxisModule import YAxis
from AxesPackage.ZAxisModule import ZAxis
from CoordinatesPackage.ThreeDCoordinatesModule import ThreeDCoordinates
from HomogeneousGridPackage.HomogeneousGridCoordinatesModule import HomogeneousGridCoordinates

class ThreeDHomogeneousGridCoordinates(HomogeneousGridCoordinates, ThreeDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [XAxis, YAxis, ZAxis],
            className = "ThreeDHomogeneousGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

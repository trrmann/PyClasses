# FourDCylindricalGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Cylindrical.ThreeDCylindricalGridCoordinates as ThreeDCylindricalGridCoordinates
import Classes.Math.Algebra.Coordinates.Grids.Axes.rAxis as rAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis as θAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.ZAxis as ZAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.TimeLine as TimeLine
import Classes.Math.Algebra.Coordinates.FourDCoordinates as FourDCoordinates

class FourDCylindricalGridCoordinates(ThreeDCylindricalGridCoordinates.ThreeDCylindricalGridCoordinates, FourDCoordinates.FourDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [rAxis.rAxis, θAxis.θAxis, ZAxis.ZAxis, TimeLine.TimeLine],
            className = "FourDCylindricalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

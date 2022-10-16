# ThreeDCylindricalGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Cylindrical.TwoDCylindricalGridCoordinates as TwoDCylindricalGridCoordinates
import Classes.Math.Algebra.Coordinates.Grids.Axes.rAxis as rAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis as θAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.ZAxis as ZAxis
import Classes.Math.Algebra.Coordinates.ThreeDCoordinates as ThreeDCoordinates

class ThreeDCylindricalGridCoordinates(TwoDCylindricalGridCoordinates.TwoDCylindricalGridCoordinates, ThreeDCoordinates.ThreeDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [rAxis.rAxis, θAxis.θAxis, ZAxis.ZAxis],
            className = "ThreeDCylindricalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

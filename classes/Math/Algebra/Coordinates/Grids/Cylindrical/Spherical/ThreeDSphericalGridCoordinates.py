# ThreeDSphericalGridCoordinates.py
import Classes.Math.Algebra.Coordinates.Grids.Cylindrical.Spherical.SphericalGridCoordinates as SphericalGridCoordinates
import Classes.Math.Algebra.Coordinates.Grids.Axes.ρAxis as ρAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.θAxis as θAxis
import Classes.Math.Algebra.Coordinates.Grids.Axes.φAxis as φAxis
import Classes.Math.Algebra.Coordinates.ThreeDCoordinates as ThreeDCoordinates

class ThreeDSphericalGridCoordinates(SphericalGridCoordinates.SphericalGridCoordinates, ThreeDCoordinates.ThreeDCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list = [ρAxis.ρAxis, θAxis.θAxis, φAxis.φAxis],
            className = "ThreeDSphericalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

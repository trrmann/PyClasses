# SphericalGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Cylindrical.CylindricalGridCoordinates import CylindricalGridCoordinates, CylindricalGridCoordinatesError

class SphericalGridCoordinatesError(CylindricalGridCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class SphericalGridCoordinates(CylindricalGridCoordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list,
            className = "SphericalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"


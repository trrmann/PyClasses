# HomogeneousGridCoordinates.py
from Classes.Math.Algebra.Coordinates.Grids.Grid import Grid

class HomogeneousGridCoordinates(Grid):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list,
            className = "HomogeneousGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

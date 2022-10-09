# Grid.py
from Classes.Math.Algebra.Coordinates.Coordinates import Coordinates, CoordinatesError

class GridError(CoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Grid(Coordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, axes_list, className = "Grid"):
        super().__init__(self, className)
        self.axes_list = axes_list

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

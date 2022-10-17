# Grid.py
from CoordinatesPackage.CoordinatesModule import Coordinates

class Grid(Coordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list,
            className = "Grid"
        ):
        super().__init__(self, className = className)
        self.axes_list = axes_list

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

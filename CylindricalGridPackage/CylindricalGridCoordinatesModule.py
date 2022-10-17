# CylindricalGridCoordinates.py
from GridsPackage.GridModule import Grid

class CylindricalGridCoordinates(Grid):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            axes_list,
            className = "CylindricalGridCoordinates"
        ):
        super().__init__(self, axes_list = axes_list, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, axes_list={self.axes_list})"

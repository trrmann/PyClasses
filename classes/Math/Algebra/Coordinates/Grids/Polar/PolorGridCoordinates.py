# PolorGridCoordinates.py
import Grid

class PolorGridCoordinatesError(Grid.GridError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class PolorGridCoordinates(Grid("PolorGridCoordinates")):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, axes_list):
        self.axes_list = axes_list

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, axes_list={self.axes_list})"

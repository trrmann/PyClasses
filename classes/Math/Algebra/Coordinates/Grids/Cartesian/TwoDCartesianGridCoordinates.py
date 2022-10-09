# TwoDCartesianGridCoordinates.py
import CartesianGridCoordinates
from Axes import XAxis
from Axes import YAxis
from TwoDCoordinates import TwoDCoordinates, TwoDCoordinatesError

class TwoDCartesianGridCoordinates(CartesianGridCoordinates.CartesianGridCoordinatesError, TwoDCoordinatesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class TwoDCartesianGridCoordinates(CartesianGridCoordinates("TwoDCartesianGridCoordinates"), TwoDCoordinates("TwoDCartesianGridCoordinates")):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, axes_list):
        self.axes_list = axes_list

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, axes_list={self.axes_list})"

# TimeLineError.py
from AxesPackage.AxisErrorModule import AxisError

class TimeLineError(AxisError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

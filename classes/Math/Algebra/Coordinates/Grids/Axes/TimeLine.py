# TimeLine.py
from Classes.Math.Algebra.Coordinates.Grids.Axes.Axis import Axis, AxisError

class TimeLineError(AxisError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

#time axis - linear axis
class TimeLine(Axis):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            t,
            className = "TimeLine"
        ):
        super().__init__(self, className = className)
        self.value = t

    def __repr__(self) -> str:
        if(self.__inf and self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, -∞, t={self.value})"
        elif(self.__inf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, t={self.value})"
        elif(self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, -∞, t={self.value})"
        else:
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, t={self.value})"

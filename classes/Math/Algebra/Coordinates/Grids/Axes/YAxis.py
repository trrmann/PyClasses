# YAxis.py
from Classes.Math.Algebra.Coordinates.Grids.Axes.Axis import Axis, AxisError
import math

class YAxisError(AxisError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

#linear axis
class YAxis(Axis("YAxis")):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, y, className = "YAxis"):
        super().__init__(self, className)
        self.value = y

    def __repr__(self) -> str:
        if(self.__inf and self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, -∞, y={self.value})"
        elif(self.__inf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, y={self.value})"
        elif(self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, -∞, y={self.value})"
        else:
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, y={self.value})"

    def radial_angular_in_wDegrees(self, r, φ):
        self.value = float(r) * math.sin(math.radians(float(φ)))
        return self

    def radial_angular_in_wRadians(self, r, φ):
        self.value = float(r) * math.sin(float(φ))
        return self

    def radial_r(self, x):
        return math.sqrt((float(x) ** 2) + (self.value ** 2))

    def angular_φ(self, x):
        return math.atan2(self.value, float(x))

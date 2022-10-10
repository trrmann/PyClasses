# XAxis.py
from Classes.Math.Algebra.Coordinates.Grids.Axes.Axis import Axis, AxisError
import math

class XAxisError(AxisError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

#linear axis
class XAxis(Axis("XAxis")):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            x,
            className = "XAxis"
        ):
        super().__init__(self, className = className)
        self.value = x

    def __repr__(self) -> str:
        if(self.__inf and self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, -∞, x={self.value})"
        elif(self.__inf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, x={self.value})"
        elif(self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, -∞, x={self.value})"
        else:
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, x={self.value})"

    def radial_angular_in_wDegrees(self, r, φ):
        self.value = float(r) * math.cos(math.radians(float(φ)))
        return self

    def radial_angular_in_wRadians(self, r, φ):
        self.value = float(r) * math.cos(float(φ))
        return self

    def radial_r(self, y):
        return math.sqrt((self.value ** 2) + (float(y) ** 2))

    def angular_φ(self, y):
        return math.atan2(float(y), self.value)

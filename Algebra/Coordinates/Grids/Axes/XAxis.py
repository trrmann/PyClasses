# XAxis.py
import Classes.Math.Algebra.Coordinates.Grids.Axes.Axis as Axis
import math

#linear axis
class XAxis(Axis.Axis):
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

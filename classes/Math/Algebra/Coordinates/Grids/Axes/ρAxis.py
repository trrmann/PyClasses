# ρAxis.py
from Classes.Math.Algebra.Coordinates.Grids.Axes.Axis import Axis, AxisError
import math

class ρAxisError(AxisError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

#radial axis to be used with an angular axis
class ρAxis(Axis):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            ρ,
            className = "ρAxis"
        ):
        super().__init__(self, className = className)
        self.value = ρ

    def __repr__(self) -> str:
        if(self.__inf and self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, -∞, ρ={self.value})"
        elif(self.__inf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, ρ={self.value})"
        elif(self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, -∞, ρ={self.value})"
        else:
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ρ={self.value})"

    def cartesian_in(self, x, y):
        self.value = math.sqrt((float(x) ** 2) + (float(y) ** 2))
        return self

    def cartesian_x_wDegrees(self, φ):
        return self.value * math.cos(math.radians(float(φ)))

    def cartesian_y_wDegrees(self, φ):
        return self.value * math.sin(math.radians(float(φ)))

    def cartesian_x_wRadians(self, φ):
        return self.value * math.cos(float(φ))

    def cartesian_y_wRadians(self, φ):
        return self.value * math.sin(float(φ))

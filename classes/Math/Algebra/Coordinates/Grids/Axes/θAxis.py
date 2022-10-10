# θAxis.py
from Classes.Math.Algebra.Coordinates.Grids.Axes.Axis import Axis, AxisError
import math

class θAxisError(AxisError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

#angular axis - 0 to 360 degrees or 0 to 2π, where + is clockwise (cw) and negative is counter-clockwise (ccw), each full revolution can be represented by an integer value.
class θAxis(Axis("θAxis")):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, θ, className = "θAxis"):
        super().__init__(self, className)
        self.value = θ

    def __repr__(self) -> str:
        if(self.__inf and self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, -∞, θ={self.value})"
        elif(self.__inf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, θ={self.value})"
        elif(self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, -∞, θ={self.value})"
        else:
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, θ={self.value})"

    def full_radians(self):
        return math.radians(self.value)

    def full_degrees(self):
        return self.value

    def radians_in(self, radians):
        self.value = math.degrees(float(radians))
        return self

    def degrees_in(self, degrees):
        self.value = float(degrees)
        return self

    def cartesian_in(self, x, y):
        self.value = math.atan2(float(y), float(x))
        return self

    def radians_out(self):
        return math.radians(self.value % 360)

    def degrees_out(self):
        return self.value % 360

    def revolutions(self):
        return int(self.value / 360)

    def cartesian_x(self, r):
        return r * math.cos(self.value)

    def cartesian_y(self, r):
        return r * math.sin(self.value)

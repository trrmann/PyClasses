# ZAxis.py
import Classes.Math.Algebra.Coordinates.Grids.Axes.Axis as Axis

#linear axis
class ZAxis(Axis.Axis):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            z,
            className = "ZAxis"
        ):
        super().__init__(self, className = className)
        self.value = z

    def __repr__(self) -> str:
        if(self.__inf and self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, -∞, z={self.value})"
        elif(self.__inf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, z={self.value})"
        elif(self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, -∞, z={self.value})"
        else:
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, z={self.value})"
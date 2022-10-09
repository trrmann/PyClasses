# ZAxis.py
import Axis

class ZAxisError(Axis.AxisError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

#linear axis
class ZAxis(Axis("ZAxis")):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, z):
        self.value = z

    def __repr__(self) -> str:
        if(self.__inf and self.__negInf):
            return f"{type(self).__name__}(name={self.name}, origin={self.__origin}, ∞, -∞, z={self.value})"
        elif(self.__inf):
            return f"{type(self).__name__}(name={self.name}, origin={self.__origin}, ∞, z={self.value})"
        elif(self.__negInf):
            return f"{type(self).__name__}(name={self.name}, origin={self.__origin}, -∞, z={self.value})"
        else:
            return f"{type(self).__name__}(name={self.name}, origin={self.__origin}, z={self.value})"

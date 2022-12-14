# Axis.py
from GridsPackage.NumberLineModule import NumberLine

class Axis(NumberLine):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            className = "Axis"
        ):
        super().__init__(self, className = className)
        pass

    def __repr__(self) -> str:
        if(self.__inf and self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, -∞, value={self.value})"
        elif(self.__inf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, ∞, value={self.value})"
        elif(self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, -∞, value={self.value})"
        else:
            return f"{type(self).__name__}(className={self.className}, origin={self.__origin}, value={self.value})"

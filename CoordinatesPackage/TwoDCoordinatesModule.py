# TwoDCoordinates.py
from CoordinatesPackage.CoordinatesModule import Coordinates

class TwoDCoordinates(Coordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "TwoDCoordinates"):
        super().__init__(self, className)
        self.__magic = "undefined"

    def __init__(self, x: float, y: float, className = "TwoDCoordinates"):
        super().__init__(self, className)
        self.__magic = "cartesian"
        self.x = x
        self.y = y

    def __init__(self, r: float, θ: float, className = "TwoDCoordinates"):
        super().__init__(self, className)
        self.__magic = "polar"
        self.r = r
        self.θ = θ

    def __init__(self, r: float, z: float, className = "TwoDCoordinates"):
        super().__init__(self, className)
        self.__magic = "cylindrical"
        self.r = r
        self.z = z

    def __repr__(self) -> str:
        match self.__magic:
            case "undefined":
                return f"{type(self).__name__}(className={self.className})"
            case "cartesian":
                return f"{type(self).__name__}(className={self.className}, x={self.x}, y={self.y})"
            case "polar":
                return f"{type(self).__name__}(className={self.className}, r={self.r}, θ={self.θ})"
            case "cylindrical":
                return f"{type(self).__name__}(className={self.className}, r={self.r}, z={self.z})"

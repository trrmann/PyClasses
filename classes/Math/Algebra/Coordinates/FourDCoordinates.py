# FourDCoordinates.py
import Classes.Math.Algebra.Coordinates.Coordinates as Coordinates

class FourDCoordinates(Coordinates.Coordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "FourDCoordinates"):
        super().__init__(self, className)
        self.__magic = "undefined"

    def __init__(self, x: float, y: float, z: float, t: float, className = "FourDCoordinates"):
        super().__init__(self, className)
        self.magic = "homogeneous"
        self.x = x
        self.z1 = z
        self.y = y
        self.z2 = z
        self.t = t
        self.z3 = z

    def __init__(self, x1: float, z1: float, y2: float, z2: float, t: float, z3: float, className = "FourDCoordinates"):
        super().__init__(self, className)
        self.magic = "cartesian"
        self.x = x1
        self.z1 = z1
        self.y = y2
        self.z2 = z2
        self.t = t
        self.z3 = z3

    def __init__(self, r: float, θ: float, z: float, t: float, className = "FourDCoordinates"):
        super().__init__(self, className)
        self.magic = "polar"
        self.r = r
        self.θ = θ
        self.z = z
        self.t = t

    """
    def __init__(self, r: float, θ: float, z: float, t: float, className = "FourDCoordinates"):
        super().__init__(self, className)
        self.magic = "cylindrical"
        self.r = r
        self.θ = θ
        self.z = z
        self.t = t
    """

    def __init__(self, ρ: float, θ: float, φ: float, t: float, className = "FourDCoordinates"):
        super().__init__(self, className)
        self.magic = "spherical"
        self.ρ = ρ
        self.θ = θ
        self.φ = φ
        self.t = t

    def __repr__(self) -> str:
        match self.__magic:
            case "undefined":
                return f"{type(self).__name__}(className={self.className})"
            case "homogeneous":
                return f"{type(self).__name__}(className={self.className}, x={self.x}, y={self.y}, z={self.z1}, t={self.t})"
            case "cartesian":
                return f"{type(self).__name__}(className={self.className}, (x={self.x}, z={self.z1}), (y={self.y}, z={self.z2}), (t={self.t}, z={self.z3}))"
            case "polar":
                return f"{type(self).__name__}(className={self.className}, r={self.r}, θ={self.θ}, z={self.z}, t={self.t})"
            case "cylindrical":
                return f"{type(self).__name__}(className={self.className}, r={self.r}, θ={self.θ}, z={self.z}, t={self.t})"
            case "spherical":
                return f"{type(self).__name__}(className={self.className}, ρ={self.ρ}, θ={self.θ}, φ={self.φ}, t={self.t})"

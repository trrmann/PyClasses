# AngleFromSides.py
from Classes.Math.Geometry.errors.MissingDimensionError import MissingDimensionError
from Classes.errors.InvalidParameterError import InvalidParameterError
import math

def AngleFromSides(angle, a: float, b: float, c: float):
    try:
        match angle:
            case "A":
                return math.asin((float(c) / math.sin(math.radians(AngleFromSides("C", float(a), float(b), float(c))))) / float(a))
            case "B":
                return math.asin((float(c) / math.sin(math.radians(AngleFromSides("C", float(a), float(b), float(c))))) / float(b))
            case "C":
                return math.degrees(math.acos(((float(a) ** 2)+(float(b) ** 2)-(float(c) ** 2)) / (2 * float(a) * float(b))))
        raise InvalidParameterError(f"Invalid Parameter Value!  angle needs to be \"A\", \"B\", or \"C\"", "AngleFromSides", "angle")
    except ValueError:
        try:
            float(a)
            try:
                float(b)
                raise MissingDimensionError(f"Missing the side c for the triangle!", "triangle", "c")
            except ValueError:
                raise MissingDimensionError(f"Missing the side b for the triangle!", "triangle", "b")
        except ValueError:
            raise MissingDimensionError(f"Missing the side a for the triangle!", "triangle", "a")

# LengthOfMedian.py
from Classes.errors.InvalidParameterError import InvalidParameterError
from Classes.Math.Geometry.errors.MissingDimensionError import MissingDimensionError
import math

def LengthOfMedian(side, a: float, b: float, c: float):
    try:
        match side:
            case "a":
                return math.sqrt(((2 * (float(b) ** 2))+(2 * (float(c) ** 2))-(float(a) ** 2))/4)
            case "b":
                return math.sqrt(((2 * (float(a) ** 2))+(2 * (float(c) ** 2))-(float(b) ** 2))/4)
            case "c":
                return math.sqrt(((2 * (float(a) ** 2))+(2 * (float(b) ** 2))-(float(c) ** 2))/4)
        raise InvalidParameterError(f"Invalid Parameter Value!  side needs to be \"a\", \"b\", or \"c\"", "LengthOfMedian", "side")
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

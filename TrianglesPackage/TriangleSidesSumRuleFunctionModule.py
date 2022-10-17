# TriangleSidesSumRule.py
from ClassesPackage.InvalidParameterErrorModule import InvalidParameterError
from GeometryPackage.MissingDimensionErrorModule import MissingDimensionError

def TriangleSidesSumRule(side, a: float, b: float, c: float):
    try:
        match side:
            case "a":
                return float(a) < (float(b) + float(c))
            case "b":
                return float(b) < (float(a) + float(c))
            case "c":
                return float(c) < (float(a) + float(b))
        raise InvalidParameterError(f"Invalid Parameter Value!  side needs to be \"a\", \"b\", or \"c\"", "TriangleSidesSumRule", "side")
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

# CircumradiusOfTriangle.py
import Classes.Math.Geometry.errors.MissingDimensionError as MissingDimensionError
import math

def CircumradiusOfTriangle(a: float, b: float, c: float):
    try:
        return float(a) / 2 * math.sin(math.acos(((float(b) ** 2)+(float(c) ** 2)-(float(a) ** 2)) / 2 * float(b) * float(c)))
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
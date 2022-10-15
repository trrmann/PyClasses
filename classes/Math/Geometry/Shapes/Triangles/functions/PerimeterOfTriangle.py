# PerimeterOfTriangle.py
from Classes.Math.Geometry.errors.MissingDimensionError import MissingDimensionError

def PerimeterOfTriangle(a: float, b: float, c: float):
    try:
        return (float(a) + float(b) + float(c))
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

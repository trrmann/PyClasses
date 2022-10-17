# BaseOfTriangle.py
from GeometryPackage.MissingDimensionErrorModule import MissingDimensionError

def BaseOfTriangle(a: float, b: float, c: float):
    try:
        return float(a)
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

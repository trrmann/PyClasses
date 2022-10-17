# doAnglesFormTriangle.py
from GeometryPackage.MissingDimensionErrorModule import MissingDimensionError

def DoAnglesFormTriangle(A: float, B: float, C: float):
    try:
        return (180) == (float(A) + float(B) + float(C))
    except ValueError:
        try:
            float(A)
            try:
                float(B)
                raise MissingDimensionError(f"Missing the angle C for the triangle!", "triangle", "C")
            except ValueError:
                raise MissingDimensionError(f"Missing the angle B for the triangle!", "triangle", "B")
        except ValueError:
            raise MissingDimensionError(f"Missing the angle A for the triangle!", "triangle", "A")

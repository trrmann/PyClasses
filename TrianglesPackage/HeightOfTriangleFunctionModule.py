# HeightOfTriangle.py
from GeometryPackage.MissingDimensionErrorModule import MissingDimensionError
from TrianglesPackage.SemiPerimeterOfTriangleFunctionModule import SemiPerimeterOfTriangle
import math

def HeightOfTriangle(a: float, b: float, c: float):
    try:
        return (2 / float(a)) * math.sqrt(SemiPerimeterOfTriangle(float(a), float(b), float(c)) * (SemiPerimeterOfTriangle(float(a), float(b), float(c)) - float(a)) * (SemiPerimeterOfTriangle(float(a), float(b), float(c)) - float(b)) * (SemiPerimeterOfTriangle(float(a), float(b), float(c)) - float(c)))
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

# AreaOfTriangle.py
from GeometryPackage.MissingDimensionErrorModule import MissingDimensionError
from TrianglesPackage.AreaOfRightTriangleFunctionModule import AreaOfRightTriangle
from TrianglesPackage.BaseOfTriangleFunctionModule import BaseOfTriangle
from TrianglesPackage.HeightOfTriangleFunctionModule import HeightOfTriangle

def AreaOfTriangle(a: float, b: float, c: float):
    try:
        return AreaOfRightTriangle(BaseOfTriangle(float(a), float(b), float(c)), HeightOfTriangle(float(a), float(b), float(c)))
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

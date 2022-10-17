# InradiusOfTriangle.py
from GeometryPackage.MissingDimensionErrorModule import MissingDimensionError
from TrianglesPackage.AreaOfTriangleFunctionModule import AreaOfTriangle
from TrianglesPackage.SemiPerimeterOfTriangleFunctionModule import SemiPerimeterOfTriangle

def InradiusOfTriangle(a: float, b: float, c: float):
    try:
        return AreaOfTriangle(float(a), float(b), float(c)) / SemiPerimeterOfTriangle(float(a), float(b), float(c))
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

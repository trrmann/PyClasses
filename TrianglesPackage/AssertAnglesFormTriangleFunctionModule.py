# AssertAnglesFormTriangle.py
from TrianglesPackage.DoAnglesFormTriangleFunctionModule import DoAnglesFormTriangle
from TrianglesPackage.TriangleErrorModule import TriangleError

def AssertAnglesFormTriangle(A: float, B: float, C: float):
    if not DoAnglesFormTriangle(A, B, C):
        raise TriangleError(f"<a: {A} + <b: {B} + <c: {C} == {A+B+C} != 180 degrees")

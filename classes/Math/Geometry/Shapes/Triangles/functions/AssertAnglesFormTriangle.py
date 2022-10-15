# AssertAnglesFormTriangle.py
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.DoAnglesFormTriangle import DoAnglesFormTriangle

def AssertAnglesFormTriangle(A: float, B: float, C: float):
    if not DoAnglesFormTriangle(A, B, C):
        raise TriangleError(f"<a: {A} + <b: {B} + <c: {C} == {A+B+C} != 180 degrees")

# AssertTriangle.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.AssertAnglesFormTriangle import AssertAnglesFormTriangle
from Classes.Math.Geometry.Shapes.Triangles.functions.AssertTriangleSidesSumRule import AssertTriangleSidesSumRule

def AssertTriangle(triangle):
    if isinstance(triangle, Triangle):
        AssertTriangleSidesSumRule(triangle.a, triangle.b, triangle.c)
        AssertAnglesFormTriangle(triangle.angle_A(), triangle.angle_B(), triangle.angle_C())
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

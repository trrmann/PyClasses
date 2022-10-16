# AssertTriangle.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.AssertAnglesFormTriangle as AssertAnglesFormTriangle
import Classes.Math.Geometry.Shapes.Triangles.functions.AssertTriangleSidesSumRule as AssertTriangleSidesSumRule

def AssertTriangle(triangle):
    if isinstance(triangle, Triangle):
        AssertTriangleSidesSumRule(triangle.a, triangle.b, triangle.c)
        AssertAnglesFormTriangle(triangle.angle_A(), triangle.angle_B(), triangle.angle_C())
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

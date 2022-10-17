# AssertTriangle.py
from TrianglesPackage.AssertAnglesFormTriangleFunctionModule import AssertAnglesFormTriangle
from TrianglesPackage.AssertTriangleSidesSumRuleFunctionModule import AssertTriangleSidesSumRule
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def AssertTriangle(triangle):
    if isinstance(triangle, Triangle):
        AssertTriangleSidesSumRule(triangle.a, triangle.b, triangle.c)
        AssertAnglesFormTriangle(triangle.angle_A(), triangle.angle_B(), triangle.angle_C())
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

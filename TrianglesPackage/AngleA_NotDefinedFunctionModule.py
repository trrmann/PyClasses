# AngleA_NotDefined.py
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def AngleA_NotDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return triangle.A == undefined
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

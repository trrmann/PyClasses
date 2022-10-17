# AngleB_NotDefined.py
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def AngleB_NotDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return triangle.B == undefined
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")
# Side_c_NotDefined.py
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def Side_c_NotDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return triangle.c == undefined
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

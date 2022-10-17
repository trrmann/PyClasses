# Side_b_NotDefined.py
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def Side_b_NotDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return triangle.b == undefined
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

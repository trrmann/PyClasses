# Side_a_NotDefined.py
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def Side_a_NotDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return triangle.a == undefined
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

# Side_a_Defined.py
from TrianglesPackage.Side_a_NotDefinedFunctionModule import Side_a_NotDefined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def Side_a_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not Side_a_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

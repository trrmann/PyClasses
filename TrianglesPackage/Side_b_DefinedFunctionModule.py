# Side_b_Defined.py
from TrianglesPackage.TriangleModule import Triangle
from TrianglesPackage.Side_b_NotDefinedFunctionModule import Side_b_NotDefined
from TrianglesPackage.TriangleErrorModule import TriangleError

def Side_b_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not Side_b_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

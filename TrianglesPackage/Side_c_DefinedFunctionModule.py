# Side_c_Defined.py
from TrianglesPackage.Side_c_NotDefinedFunctionModule import Side_c_NotDefined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def Side_c_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not Side_c_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

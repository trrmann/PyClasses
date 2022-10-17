# AngleA_Defined.py
from TrianglesPackage.AngleA_NotDefinedFunctionModule import AngleA_NotDefined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def AngleA_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not AngleA_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

# AngleC_Defined.py
from TrianglesPackage.AngleC_NotDefinedFunctionModule import AngleC_NotDefined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def AngleC_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not AngleC_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

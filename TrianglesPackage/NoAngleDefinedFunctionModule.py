# NoAngleDefined.py
from TrianglesPackage.AngleA_NotDefinedFunctionModule import AngleA_NotDefined
from TrianglesPackage.AngleB_NotDefinedFunctionModule import AngleB_NotDefined
from TrianglesPackage.AngleC_NotDefinedFunctionModule import AngleC_NotDefined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def NoAngleDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return AngleA_NotDefined(triangle, undefined) and AngleB_NotDefined(triangle, undefined) and AngleC_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

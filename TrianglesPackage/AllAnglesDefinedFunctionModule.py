# AllAnglesDefined.py
from TrianglesPackage.AngleA_DefinedFunctionModule import AngleA_Defined
from TrianglesPackage.AngleB_DefinedFunctionModule import AngleB_Defined
from TrianglesPackage.AngleC_DefinedFunctionModule import AngleC_Defined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def AllAnglesDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

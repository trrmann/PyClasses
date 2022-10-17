# AllSidesDefined.py
from TrianglesPackage.Side_a_DefinedFunctionModule import Side_a_Defined
from TrianglesPackage.Side_b_DefinedFunctionModule import Side_b_Defined
from TrianglesPackage.Side_c_DefinedFunctionModule import Side_c_Defined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def AllSidesDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

# NoSideDefined.py
from TrianglesPackage.Side_a_NotDefinedFunctionModule import Side_a_NotDefined
from TrianglesPackage.Side_b_NotDefinedFunctionModule import Side_b_NotDefined
from TrianglesPackage.Side_c_NotDefinedFunctionModule import Side_c_NotDefined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def NoSideDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return Side_a_NotDefined(triangle, undefined) and Side_b_NotDefined(triangle, undefined) and Side_c_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

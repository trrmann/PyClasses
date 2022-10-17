# HasAngleDefined.py
from TrianglesPackage.NoAngleDefinedFunctionModule import NoAngleDefined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def HasAngleDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not NoAngleDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

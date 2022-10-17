# HasSideDefined.py
from TrianglesPackage.NoSideDefinedFunctionModule import NoSideDefined
from TrianglesPackage.TriangleErrorModule import TriangleError
from TrianglesPackage.TriangleModule import Triangle

def HasSideDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not NoSideDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

# AngleA_Defined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleA_NotDefined import AngleA_NotDefined

def AngleA_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not AngleA_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

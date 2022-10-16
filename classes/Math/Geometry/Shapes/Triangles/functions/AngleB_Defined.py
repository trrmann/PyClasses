# AngleB_Defined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleB_NotDefined import AngleB_NotDefined

def AngleB_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not AngleB_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")


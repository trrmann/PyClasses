# NoAngleDefined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleA_NotDefined import AngleA_NotDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleB_NotDefined import AngleB_NotDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleC_NotDefined import AngleC_NotDefined

def NoAngleDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return AngleA_NotDefined(triangle, undefined) and AngleB_NotDefined(triangle, undefined) and AngleC_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

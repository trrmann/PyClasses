# HasAngleDefined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.NoAngleDefined import NoAngleDefined

def HasAngleDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not NoAngleDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

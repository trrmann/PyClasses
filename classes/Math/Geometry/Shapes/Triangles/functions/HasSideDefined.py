# HasSideDefined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.NoSideDefined import NoSideDefined

def HasSideDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not NoSideDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

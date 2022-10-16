# Side_c_NotDefined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError

def Side_c_NotDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return triangle.c == undefined
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

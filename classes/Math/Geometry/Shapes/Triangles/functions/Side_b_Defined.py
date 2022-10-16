# Side_b_Defined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_b_NotDefined import Side_b_NotDefined

def Side_b_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not Side_b_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

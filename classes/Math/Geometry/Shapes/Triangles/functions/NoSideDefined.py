# NoSideDefined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_a_NotDefined import Side_a_NotDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_b_NotDefined import Side_b_NotDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_c_NotDefined import Side_c_NotDefined

def NoSideDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return Side_a_NotDefined(triangle, undefined) and Side_b_NotDefined(triangle, undefined) and Side_c_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

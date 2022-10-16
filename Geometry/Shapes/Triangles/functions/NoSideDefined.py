# NoSideDefined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.Side_a_NotDefined as Side_a_NotDefined
import Classes.Math.Geometry.Shapes.Triangles.functions.Side_b_NotDefined as Side_b_NotDefined
import Classes.Math.Geometry.Shapes.Triangles.functions.Side_c_NotDefined as Side_c_NotDefined

def NoSideDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return Side_a_NotDefined(triangle, undefined) and Side_b_NotDefined(triangle, undefined) and Side_c_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

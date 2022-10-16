# Side_b_Defined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.Side_b_NotDefined as Side_b_NotDefined

def Side_b_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not Side_b_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

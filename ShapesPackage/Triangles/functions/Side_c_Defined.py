# Side_c_Defined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.Side_c_NotDefined as Side_c_NotDefined

def Side_c_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not Side_c_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

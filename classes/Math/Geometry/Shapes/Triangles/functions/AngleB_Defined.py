# AngleB_Defined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.AngleB_NotDefined as AngleB_NotDefined

def AngleB_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not AngleB_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")


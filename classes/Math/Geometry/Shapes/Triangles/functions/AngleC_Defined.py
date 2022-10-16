# AngleC_Defined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.AngleC_NotDefined as AngleC_NotDefined

def AngleC_Defined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not AngleC_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

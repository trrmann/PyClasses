# AngleC_NotDefined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError

def AngleC_NotDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return triangle.C == undefined
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

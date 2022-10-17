# AngleB_NotDefined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError

def AngleB_NotDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return triangle.B == undefined
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")
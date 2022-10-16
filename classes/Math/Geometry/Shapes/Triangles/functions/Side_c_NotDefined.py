# Side_c_NotDefined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError

def Side_c_NotDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return triangle.c == undefined
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

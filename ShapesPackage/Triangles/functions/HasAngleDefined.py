# HasAngleDefined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.NoAngleDefined as NoAngleDefined

def HasAngleDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return not NoAngleDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

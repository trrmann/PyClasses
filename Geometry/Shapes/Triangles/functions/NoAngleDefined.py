# NoAngleDefined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.AngleA_NotDefined as AngleA_NotDefined
import Classes.Math.Geometry.Shapes.Triangles.functions.AngleB_NotDefined as AngleB_NotDefined
import Classes.Math.Geometry.Shapes.Triangles.functions.AngleC_NotDefined as AngleC_NotDefined

def NoAngleDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return AngleA_NotDefined(triangle, undefined) and AngleB_NotDefined(triangle, undefined) and AngleC_NotDefined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

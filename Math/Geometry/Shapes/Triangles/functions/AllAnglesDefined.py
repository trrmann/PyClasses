# AllAnglesDefined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.AngleA_Defined as AngleA_Defined
import Classes.Math.Geometry.Shapes.Triangles.functions.AngleB_Defined as AngleB_Defined
import Classes.Math.Geometry.Shapes.Triangles.functions.AngleC_Defined as AngleC_Defined

def AllAnglesDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

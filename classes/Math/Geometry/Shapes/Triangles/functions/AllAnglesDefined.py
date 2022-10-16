# AllAnglesDefined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleA_Defined import AngleA_Defined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleB_Defined import AngleB_Defined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleC_Defined import AngleC_Defined

def AllAnglesDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

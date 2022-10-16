# AllSidesDefined.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_a_Defined import Side_a_Defined
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_b_Defined import Side_b_Defined
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_c_Defined import Side_c_Defined

def AllSidesDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

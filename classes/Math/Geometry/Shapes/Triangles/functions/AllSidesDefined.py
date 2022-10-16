# AllSidesDefined.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
import Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError as TriangleError
import Classes.Math.Geometry.Shapes.Triangles.functions.Side_a_Defined as Side_a_Defined
import Classes.Math.Geometry.Shapes.Triangles.functions.Side_b_Defined as Side_b_Defined
import Classes.Math.Geometry.Shapes.Triangles.functions.Side_c_Defined as Side_c_Defined

def AllSidesDefined(triangle, undefined):
    if isinstance(triangle, Triangle):
        return Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined)
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

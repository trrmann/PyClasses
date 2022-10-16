# SolveTriangle.py
import Classes.Math.Geometry.Shapes.Triangles.Triangle as Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.AllAnglesDefined import AllAnglesDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.AllSidesDefined import AllSidesDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleA_Defined import AngleA_Defined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleA_NotDefined import AngleA_NotDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleB_Defined import AngleB_Defined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleB_NotDefined import AngleB_NotDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleC_Defined import AngleC_Defined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleC_NotDefined import AngleC_NotDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleFromSides import AngleFromSides
from Classes.Math.Geometry.Shapes.Triangles.functions.HasAngleDefined import HasAngleDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.HasSideDefined import HasSideDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.NoAngleDefined import NoAngleDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.NoSideDefined import NoSideDefined
from Classes.Math.Geometry.Shapes.Triangles.functions.OppositeAngleFromSideSideExteriorAngle import OppositeAngleFromSideSideExteriorAngle
from Classes.Math.Geometry.Shapes.Triangles.functions.OppositeSideFromAngleAngleExteriorSide import OppositeSideFromAngleAngleExteriorSide
from Classes.Math.Geometry.Shapes.Triangles.functions.OppositeSideFromSideSideInteriorAngle import OppositeSideFromSideSideInteriorAngle
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_a_Defined import Side_a_Defined
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_b_Defined import Side_b_Defined
from Classes.Math.Geometry.Shapes.Triangles.functions.Side_c_Defined import Side_c_Defined
from Classes.Math.Geometry.errors.MissingDimensionError import MissingDimensionError

def SolveTriangle(triangle, undefined):
    if isinstance(triangle, Triangle):
        if NoSideDefined(triangle, undefined) and NoAngleDefined(triangle, undefined):
            # no data *** Done ***
            return triangle
        elif NoSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined):
            # has all three angles and no sides *** Done ***
            return triangle
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # no sides and has angle A and B but not angle C
            try:
                triangle.C = 180 - float(triangle.A) - float(triangle.B)
                return triangle
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # no sides and has angle A and C but not angle B
            try:
                triangle.B = 180 - float(triangle.A) - float(triangle.C)
                return triangle
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleA_Defined(triangle, undefined):
            # no sides and only has angle A *** Done ***
            return triangle
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # no sides and has angle B and C but not angle A
            try:
                triangle.A = 180 - float(triangle.B) - float(triangle.C)
                return triangle
            except ValueError:
                try:
                    float(triangle.B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # no sides and only has angle B *** Done ***
            return triangle
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined):
            # no sides and only has angle C *** Done ***
            return triangle
        elif AllSidesDefined(triangle, undefined) and NoAngleDefined(triangle, undefined):
            # has all three sides and no angles
            try:
                triangle.A = AngleFromSides("A", float(triangle.a), float(triangle.b), float(triangle.c))
                triangle.B = AngleFromSides("B", float(triangle.a), float(triangle.b), float(triangle.c))
                triangle.C = AngleFromSides("C", float(triangle.a), float(triangle.b), float(triangle.c))
                return triangle
            except ValueError:
                try:
                    float(triangle.a)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
        elif HasSideDefined(triangle, undefined) and NoAngleDefined(triangle, undefined):
            # only 1 or 2 sides and no angles *** Done ***
            return triangle
        elif AllSidesDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined):
            # has all 3 angles and all three sides *** Done ***
            return triangle
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleA_NotDefined(triangle, undefined) and AngleB_NotDefined(triangle, undefined):
            try:
                triangle.A = AngleFromSides("A", float(triangle.a), float(triangle.b), float(triangle.c))
                triangle.B = AngleFromSides("B", float(triangle.a), float(triangle.b), float(triangle.c))
                return triangle
            except ValueError:
                try:
                    float(triangle.a)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleA_NotDefined(triangle, undefined) and AngleC_NotDefined(triangle, undefined):
            try:
                triangle.A = AngleFromSides("A", float(triangle.a), float(triangle.b), float(triangle.c))
                triangle.C = AngleFromSides("C", float(triangle.a), float(triangle.b), float(triangle.c))
                return triangle
            except ValueError:
                try:
                    float(triangle.a)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleB_NotDefined(triangle, undefined) and AngleC_NotDefined(triangle, undefined):
            try:
                triangle.B = AngleFromSides("B", float(triangle.a), float(triangle.b), float(triangle.c))
                triangle.C = AngleFromSides("C", float(triangle.a), float(triangle.b), float(triangle.c))
                return triangle
            except ValueError:
                try:
                    float(triangle.a)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleA_NotDefined(triangle, undefined):
            try:
                triangle.A = AngleFromSides("A", float(triangle.a), float(triangle.b), float(triangle.c))
                return triangle
            except ValueError:
                try:
                    float(triangle.a)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleB_NotDefined(triangle, undefined):
            try:
                triangle.B = AngleFromSides("B", float(triangle.a), float(triangle.b), float(triangle.c))
                return triangle
            except ValueError:
                try:
                    float(triangle.a)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleC_NotDefined(triangle, undefined):
            try:
                triangle.C = AngleFromSides("C", float(triangle.a), float(triangle.b), float(triangle.c))
                return triangle
            except ValueError:
                try:
                    float(triangle.a)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined):
            # have all three angles and side a and side b
            try:
                triangle.c = OppositeSideFromAngleAngleExteriorSide(float(triangle.C), float(triangle.A), float(triangle.a))
                return triangle
            except ValueError:
                try:
                    float(triangle.C)
                    try:
                        float(triangle.A)
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined):
            # have all three angles and side a and side c
            try:
                triangle.b = OppositeSideFromAngleAngleExteriorSide(float(triangle.B), float(triangle.A), float(triangle.a))
                return triangle
            except ValueError:
                try:
                    float(triangle.B)
                    try:
                        float(triangle.A)
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined):
            # have all three angles and side b and side c
            try:
                triangle.a = OppositeSideFromAngleAngleExteriorSide(float(triangle.A), float(triangle.B), float(triangle.b))
                return triangle
            except ValueError:
                try:
                    float(triangle.A)
                    try:
                        float(triangle.B)
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and Side_a_Defined(triangle, undefined):
            # have all three angles and only side a
            try:
                triangle.c = OppositeSideFromAngleAngleExteriorSide(float(triangle.C), float(triangle.A), float(triangle.a))
                try:
                    triangle.b = OppositeSideFromAngleAngleExteriorSide(float(triangle.B), float(triangle.A), float(triangle.a))
                    return triangle
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
            except ValueError:
                try:
                    float(triangle.C)
                    try:
                        float(triangle.A)
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and Side_b_Defined(triangle, undefined):
            # have all three angles and only side b
            try:
                triangle.c = OppositeSideFromAngleAngleExteriorSide(float(triangle.C), float(triangle.B), float(triangle.b))
                try:
                    triangle.a = OppositeSideFromAngleAngleExteriorSide(float(triangle.A), float(triangle.B), float(triangle.b))
                    return triangle
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
            except ValueError:
                try:
                    float(triangle.C)
                    try:
                        float(triangle.B)
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined):
            # have all three angles and only side c
            try:
                triangle.a = OppositeSideFromAngleAngleExteriorSide(float(triangle.A), float(triangle.C), float(triangle.c))
                try:
                    triangle.b = OppositeSideFromAngleAngleExteriorSide(float(triangle.B), float(triangle.C), float(triangle.c))
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                return triangle
            except ValueError:
                try:
                    float(triangle.A)
                    try:
                        float(triangle.C)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle A and angle B and side a and side b
            try:
                triangle.C = 180 - float(triangle.A) - float(triangle.B)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle A and angle C and side a and side b
            try:
                triangle.B = 180 - float(triangle.A) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle B and angle C and side a and side b
            try:
                triangle.A = 180 - float(triangle.B) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined):
            # have angle A and side a and side b
            try:
                triangle.B = OppositeAngleFromSideSideExteriorAngle(float(triangle.b), float(triangle.a), float(triangle.A))
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.b)
                    try:
                        float(triangle.a)
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle B and side a and side b
            try:
                triangle.A = OppositeAngleFromSideSideExteriorAngle(float(triangle.a), float(triangle.b), float(triangle.B))
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.a)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_b_Defined(triangle, undefined):
            # have angle C and side a and side b
            try:
                triangle.c = OppositeSideFromSideSideInteriorAngle(float(triangle.C), float(triangle.a), float(triangle.b))
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.C)
                    try:
                        float(triangle.a)
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle A and angle B and side a and side c
            try:
                triangle.C = 180 - float(triangle.A) - float(triangle.B)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle A and angle C and side a and side c
            try:
                triangle.B = 180 - float(triangle.A) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle B and angle C and side a and side c
            try:
                triangle.A = 180 - float(triangle.B) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined):
            # have angle A and side a and side c
            try:
                triangle.C = OppositeAngleFromSideSideExteriorAngle(float(triangle.c), float(triangle.a), float(triangle.A))
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.c)
                    try:
                        float(triangle.a)
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle B and side a and side c
            try:
                triangle.b = OppositeSideFromSideSideInteriorAngle(float(triangle.B), float(triangle.a), float(triangle.c))
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.B)
                    try:
                        float(triangle.a)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined):
            # have angle C and side a and side c
            try:
                triangle.A = OppositeAngleFromSideSideExteriorAngle(float(triangle.a), float(triangle.c), float(triangle.C))
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.a)
                    try:
                        float(triangle.c)
                        raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({triangle.a})", "Triangle AutoDetermine", "a")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle A and angle B and side b and side c
            try:
                triangle.C = 180 - float(triangle.A) - float(triangle.B)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle A and angle C and side b and side c
            try:
                triangle.B = 180 - float(triangle.A) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle B and angle C and side b and side c
            try:
                triangle.A = 180 - float(triangle.B) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined):
            # have angle A and side b and side c
            try:
                triangle.a = OppositeSideFromSideSideInteriorAngle(float(triangle.A), float(triangle.b), float(triangle.c))
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle B and side b and side c
            try:
                triangle.C = OppositeAngleFromSideSideExteriorAngle(float(triangle.c), float(triangle.b), float(triangle.B))
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.c)
                    try:
                        float(triangle.b)
                        raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and Side_c_Defined(triangle, undefined):
            # have angle C and side b and side c
            try:
                triangle.B = OppositeAngleFromSideSideExteriorAngle(float(triangle.b), float(triangle.c), float(triangle.C))
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.b)
                    try:
                        float(triangle.c)
                        raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({triangle.c})", "Triangle AutoDetermine", "c")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side b for the triangle!  received({triangle.b})", "Triangle AutoDetermine", "b")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle A and angle B and side a
            try:
                triangle.C = 180 - float(triangle.A) - float(triangle.B)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle A and angle C and side a
            try:
                triangle.B = 180 - float(triangle.A) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle B and angle C and side a
            try:
                triangle.A = 180 - float(triangle.B) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined):
            # have angle A and side a *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle B and side a *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_a_Defined(triangle, undefined):
            # have angle C and side a *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle A and angle B and side b
            try:
                triangle.C = 180 - float(triangle.A) - float(triangle.B)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle A and angle C and side b
            try:
                triangle.B = 180 - float(triangle.A) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle B and angle C and side b
            try:
                triangle.A = 180 - float(triangle.B) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleA_Defined(triangle, undefined):
            # have angle A and side b *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle B and side b *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and Side_b_Defined(triangle, undefined):
            # have angle C and side b *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle A and angle B and side c
            try:
                triangle.C = 180 - float(triangle.A) - float(triangle.B)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleA_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle A and angle C and side c
            try:
                triangle.B = 180 - float(triangle.A) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({triangle.A})", "Triangle AutoDetermine", "A")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleB_Defined(triangle, undefined) and AngleC_Defined(triangle, undefined):
            # have angle B and angle C and side c
            try:
                triangle.A = 180 - float(triangle.B) - float(triangle.C)
                return SolveTriangle(triangle, undefined)
            except ValueError:
                try:
                    float(triangle.B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({triangle.C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({triangle.B})", "Triangle AutoDetermine", "B")
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleA_Defined(triangle, undefined):
            # have angle A and side c *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and AngleB_Defined(triangle, undefined):
            # have angle B and side c *** Done ***
            return triangle
        #elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined):
        else:
            # have angle C and side c *** Done ***
            return triangle
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

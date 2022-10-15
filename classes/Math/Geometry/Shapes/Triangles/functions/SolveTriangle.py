# SolveTriangle.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleFromSides import AngleFromSides
from Classes.Math.Geometry.Shapes.Triangles.functions.OppositeAngleFromSideSideExteriorAngle import OppositeAngleFromSideSideExteriorAngle
from Classes.Math.Geometry.Shapes.Triangles.functions.OppositeSideFromAngleAngleExteriorSide import OppositeSideFromAngleAngleExteriorSide
from Classes.Math.Geometry.Shapes.Triangles.functions.OppositeSideFromSideSideInteriorAngle import OppositeSideFromSideSideInteriorAngle
from Classes.Math.Geometry.errors.MissingDimensionError import MissingDimensionError

def A_NotDefined(triangle, undefined):
    return triangle.A == undefined

def B_NotDefined(triangle, undefined):
    return triangle.B == undefined

def C_NotDefined(triangle, undefined):
    return triangle.C == undefined

def A_Defined(triangle, undefined):
    return not A_NotDefined(triangle, undefined)

def B_Defined(triangle, undefined):
    return not B_NotDefined(triangle, undefined)

def C_Defined(triangle, undefined):
    return not C_NotDefined(triangle, undefined)

def a_NotDefined(triangle, undefined):
    return triangle.a == undefined

def b_NotDefined(triangle, undefined):
    return triangle.b == undefined

def c_NotDefined(triangle, undefined):
    return triangle.c == undefined

def a_Defined(triangle, undefined):
    return not a_NotDefined(triangle, undefined)

def b_Defined(triangle, undefined):
    return not b_NotDefined(triangle, undefined)

def c_Defined(triangle, undefined):
    return not c_NotDefined(triangle, undefined)

def NoSideDefined(triangle, undefined):
    return a_NotDefined(triangle, undefined) and b_NotDefined(triangle, undefined) and c_NotDefined(triangle, undefined)

def HasSideDefined(triangle, undefined):
    return not NoSideDefined(triangle, undefined)

def AllSidesDefined(triangle, undefined):
    return a_Defined(triangle, undefined) and b_Defined(triangle, undefined) and c_Defined(triangle, undefined)

def NoAngleDefined(triangle, undefined):
    return A_NotDefined(triangle, undefined) and B_NotDefined(triangle, undefined) and C_NotDefined(triangle, undefined)

def HasAngleDefined(triangle, undefined):
    return not NoAngleDefined(triangle, undefined)

def AllAnglesDefined(triangle, undefined):
    return A_Defined(triangle, undefined) and B_Defined(triangle, undefined) and C_Defined(triangle, undefined)

def SolveTriangle(triangle, undefined):
    if isinstance(triangle, Triangle):
        a = triangle.a
        b = triangle.b
        c = triangle.c
        A = triangle.A
        B = triangle.B
        C = triangle.C
        if NoSideDefined(triangle, undefined) and NoAngleDefined(triangle, undefined):
            # no data *** Done ***
            return triangle
        elif NoSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined):
            # has all three angles and no sides *** Done ***
            return triangle
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and A_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # no sides and has angle A and B but not angle C
            try:
                C = 180 - float(A) - float(B)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.C = C
            return triangle
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and A_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # no sides and has angle A and C but not angle B
            try:
                B = 180 - float(A) - float(C)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.B = B
            return triangle
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and A_Defined(triangle, undefined):
            # no sides and only has angle A *** Done ***
            return triangle
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and B_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # no sides and has angle B and C but not angle A
            try:
                A = 180 - float(B) - float(C)
            except ValueError:
                try:
                    float(B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.A = A
            return triangle
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and B_Defined(triangle, undefined):
            # no sides and only has angle B *** Done ***
            return triangle
        elif NoSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined):
            # no sides and only has angle C *** Done ***
            return triangle
        elif AllSidesDefined(triangle, undefined) and NoAngleDefined(triangle, undefined):
            # has all three sides and no angles
            try:
                A = AngleFromSides("A", float(a), float(b), float(c))
                triangle.A = A
                B = AngleFromSides("B", float(a), float(b), float(c))
                triangle.B = B
                C = AngleFromSides("C", float(a), float(b), float(c))
                triangle.C = C
                return triangle
            except ValueError:
                try:
                    float(a)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
        elif HasSideDefined(triangle, undefined) and NoAngleDefined(triangle, undefined):
            # only 1 or 2 sides and no angles *** Done ***
            return triangle
        elif AllSidesDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined):
            # has all 3 angles and all three sides *** Done ***
            return triangle
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and A_NotDefined(triangle, undefined) and B_NotDefined(triangle, undefined):
            try:
                A = AngleFromSides("A", float(a), float(b), float(c))
                B = AngleFromSides("B", float(a), float(b), float(c))
            except ValueError:
                try:
                    float(a)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
            triangle.A = A
            triangle.B = B
            return triangle
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and A_NotDefined(triangle, undefined) and C_NotDefined(triangle, undefined):
            try:
                A = AngleFromSides("A", float(a), float(b), float(c))
                C = AngleFromSides("C", float(a), float(b), float(c))
            except ValueError:
                try:
                    float(a)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
            triangle.A = A
            triangle.C = C
            return triangle
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and B_NotDefined(triangle, undefined) and C_NotDefined(triangle, undefined):
            try:
                B = AngleFromSides("B", float(a), float(b), float(c))
                C = AngleFromSides("C", float(a), float(b), float(c))
            except ValueError:
                try:
                    float(a)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
            triangle.B = B
            triangle.C = C
            return triangle
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and A_NotDefined(triangle, undefined):
            try:
                A = AngleFromSides("A", float(a), float(b), float(c))
            except ValueError:
                try:
                    float(a)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
            triangle.A = A
            return triangle
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and B_NotDefined(triangle, undefined):
            try:
                B = AngleFromSides("B", float(a), float(b), float(c))
            except ValueError:
                try:
                    float(a)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
            triangle.B = B
            return triangle
        elif AllSidesDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and C_NotDefined(triangle, undefined):
            try:
                C = AngleFromSides("C", float(a), float(b), float(c))
            except ValueError:
                try:
                    float(a)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
            triangle.C = C
            return triangle
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and a_Defined(triangle, undefined) and b_Defined(triangle, undefined):
            # have all three angles and side a and side b
            try:
                c = OppositeSideFromAngleAngleExteriorSide(float(C), float(A), float(a))
            except ValueError:
                try:
                    float(C)
                    try:
                        float(A)
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
            triangle.c = c 
            return triangle
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and a_Defined(triangle, undefined) and c_Defined(triangle, undefined):
            # have all three angles and side a and side c
            try:
                b = OppositeSideFromAngleAngleExteriorSide(float(B), float(A), float(a))
            except ValueError:
                try:
                    float(B)
                    try:
                        float(A)
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.b = b 
            return triangle
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and b_Defined(triangle, undefined) and c_Defined(triangle, undefined):
            # have all three angles and side b and side c
            try:
                a = OppositeSideFromAngleAngleExteriorSide(float(A), float(B), float(b))
            except ValueError:
                try:
                    float(A)
                    try:
                        float(B)
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.a = a 
            return triangle
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and a_Defined(triangle, undefined):
            # have all three angles and only side a
            try:
                c = OppositeSideFromAngleAngleExteriorSide(float(C), float(A), float(a))
            except ValueError:
                try:
                    float(C)
                    try:
                        float(A)
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
            triangle.c = c 
            try:
                b = OppositeSideFromAngleAngleExteriorSide(float(B), float(A), float(a))
            except ValueError:
                try:
                    float(B)
                    try:
                        float(A)
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.b = b 
            return triangle
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined) and b_Defined(triangle, undefined):
            # have all three angles and only side b
            try:
                c = OppositeSideFromAngleAngleExteriorSide(float(C), float(B), float(b))
            except ValueError:
                try:
                    float(C)
                    try:
                        float(B)
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
            triangle.c = c 
            try:
                a = OppositeSideFromAngleAngleExteriorSide(float(A), float(B), float(b))
            except ValueError:
                try:
                    float(A)
                    try:
                        float(B)
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.a = a 
            return triangle
        elif HasSideDefined(triangle, undefined) and AllAnglesDefined(triangle, undefined):
            # have all three angles and only side c
            try:
                a = OppositeSideFromAngleAngleExteriorSide(float(A), float(C), float(c))
            except ValueError:
                try:
                    float(A)
                    try:
                        float(C)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.a = a
            try:
                b = OppositeSideFromAngleAngleExteriorSide(float(B), float(C), float(c))
            except ValueError:
                try:
                    float(B)
                    try:
                        float(C)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.b = b
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and b_Defined(triangle, undefined) and A_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle A and angle B and side a and side b
            try:
                C = 180 - float(A) - float(B)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.C = C
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and b_Defined(triangle, undefined) and A_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle A and angle C and side a and side b
            try:
                B = 180 - float(A) - float(C)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.B = B
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and b_Defined(triangle, undefined) and B_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle B and angle C and side a and side b
            try:
                A = 180 - float(B) - float(C)
            except ValueError:
                try:
                    float(B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.A = A
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and b_Defined(triangle, undefined) and A_Defined(triangle, undefined):
            # have angle A and side a and side b
            try:
                B = OppositeAngleFromSideSideExteriorAngle(float(b), float(a), float(A))
            except ValueError:
                try:
                    float(b)
                    try:
                        float(a)
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
            triangle.B = B
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and b_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle B and side a and side b
            try:
                A = OppositeAngleFromSideSideExteriorAngle(float(a), float(b), float(B))
            except ValueError:
                try:
                    float(a)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
            triangle.A = A
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and b_Defined(triangle, undefined):
            # have angle C and side a and side b
            try:
                c = OppositeSideFromSideSideInteriorAngle(float(C), float(a), float(b))
            except ValueError:
                try:
                    float(C)
                    try:
                        float(a)
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
            triangle.c = c
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and c_Defined(triangle, undefined) and A_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle A and angle B and side a and side c
            try:
                C = 180 - float(A) - float(B)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.C = C
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and c_Defined(triangle, undefined) and A_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle A and angle C and side a and side c
            try:
                B = 180 - float(A) - float(C)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.B = B
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and c_Defined(triangle, undefined) and B_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle B and angle C and side a and side c
            try:
                A = 180 - float(B) - float(C)
            except ValueError:
                try:
                    float(B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.A = A
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and c_Defined(triangle, undefined) and A_Defined(triangle, undefined):
            # have angle A and side a and side c
            try:
                C = OppositeAngleFromSideSideExteriorAngle(float(c), float(a), float(A))
            except ValueError:
                try:
                    float(c)
                    try:
                        float(a)
                        raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
            triangle.C = C
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and c_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle B and side a and side c
            try:
                b = OppositeSideFromSideSideInteriorAngle(float(B), float(a), float(c))
            except ValueError:
                try:
                    float(B)
                    try:
                        float(a)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.b = b
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and c_Defined(triangle, undefined):
            # have angle C and side a and side c
            try:
                A = OppositeAngleFromSideSideExteriorAngle(float(a), float(c), float(C))
            except ValueError:
                try:
                    float(a)
                    try:
                        float(c)
                        raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side a for the triangle!  received({a})", "Triangle AutoDetermine", "a")
            triangle.A = A
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and c_Defined(triangle, undefined) and A_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle A and angle B and side b and side c
            try:
                C = 180 - float(A) - float(B)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.C = C
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and c_Defined(triangle, undefined) and A_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle A and angle C and side b and side c
            try:
                B = 180 - float(A) - float(C)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.B = B
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and c_Defined(triangle, undefined) and B_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle B and angle C and side b and side c
            try:
                A = 180 - float(B) - float(C)
            except ValueError:
                try:
                    float(B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.A = A
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and c_Defined(triangle, undefined) and A_Defined(triangle, undefined):
            # have angle A and side b and side c
            try:
                a = OppositeSideFromSideSideInteriorAngle(float(A), float(b), float(c))
            except ValueError:
                try:
                    float(A)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.a = a
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and c_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle B and side b and side c
            try:
                C = OppositeAngleFromSideSideExteriorAngle(float(c), float(b), float(B))
            except ValueError:
                try:
                    float(c)
                    try:
                        float(b)
                        raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
            triangle.C = C
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and c_Defined(triangle, undefined):
            # have angle C and side b and side c
            try:
                B = OppositeAngleFromSideSideExteriorAngle(float(b), float(c), float(C))
            except ValueError:
                try:
                    float(b)
                    try:
                        float(c)
                        raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                    except ValueError:
                        raise MissingDimensionError(f"Missing the side c for the triangle!  received({c})", "Triangle AutoDetermine", "c")
                except ValueError:
                    raise MissingDimensionError(f"Missing the side b for the triangle!  received({b})", "Triangle AutoDetermine", "b")
            triangle.B = B
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and A_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle A and angle B and side a
            try:
                C = 180 - float(A) - float(B)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.C = C
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and A_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle A and angle C and side a
            try:
                B = 180 - float(A) - float(C)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.B = B
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and B_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle B and angle C and side a
            try:
                A = 180 - float(B) - float(C)
            except ValueError:
                try:
                    float(B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.A = A
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and A_Defined(triangle, undefined):
            # have angle A and side a *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle B and side a *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and a_Defined(triangle, undefined):
            # have angle C and side a *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and A_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle A and angle B and side b
            try:
                C = 180 - float(A) - float(B)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.C = C
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and A_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle A and angle C and side b
            try:
                B = 180 - float(A) - float(C)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.B = B
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and B_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle B and angle C and side b
            try:
                A = 180 - float(B) - float(C)
            except ValueError:
                try:
                    float(B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.A = A
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and A_Defined(triangle, undefined):
            # have angle A and side b *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle B and side b *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and b_Defined(triangle, undefined):
            # have angle C and side b *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and A_Defined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle A and angle B and side c
            try:
                C = 180 - float(A) - float(B)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.C = C
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and A_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle A and angle C and side c
            try:
                B = 180 - float(A) - float(C)
            except ValueError:
                try:
                    float(A)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle A for the triangle!  received({A})", "Triangle AutoDetermine", "A")
            triangle.B = B
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and B_Defined(triangle, undefined) and C_Defined(triangle, undefined):
            # have angle B and angle C and side c
            try:
                A = 180 - float(B) - float(C)
            except ValueError:
                try:
                    float(B)
                    raise MissingDimensionError(f"Missing the angle C for the triangle!  received({C})", "Triangle AutoDetermine", "C")
                except ValueError:
                    raise MissingDimensionError(f"Missing the angle B for the triangle!  received({B})", "Triangle AutoDetermine", "B")
            triangle.A = A
            return SolveTriangle(triangle, undefined)
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and A_Defined(triangle, undefined):
            # have angle A and side c *** Done ***
            return triangle
        elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined) and B_Defined(triangle, undefined):
            # have angle B and side c *** Done ***
            return triangle
        #elif HasSideDefined(triangle, undefined) and HasAngleDefined(triangle, undefined):
        else:
            # have angle C and side c *** Done ***
            return triangle
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

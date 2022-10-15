# SolveTriangle.py
from Classes.Math.Geometry.Shapes.Triangles.Triangle import Triangle
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleFromSides import AngleFromSides
from Classes.Math.Geometry.Shapes.Triangles.functions.OppositeSideFromAngleAngleExteriorSide import OppositeSideFromAngleAngleExteriorSide
from Classes.Math.Geometry.errors.MissingDimensionError import MissingDimensionError

def NoSideDefined(triangle, undefined):
    return triangle.a == undefined and triangle.b == undefined and triangle.c == undefined

def AllSidesDefined(triangle, undefined):
    return not(triangle.a == undefined) and not(triangle.b == undefined) and not(triangle.c == undefined)

def NoAngleDefined(triangle, undefined):
    return triangle.A == undefined and triangle.B == undefined and triangle.C == undefined

def AllAnglesDefined(triangle, undefined):
    return not(triangle.A == undefined) and not(triangle.B == undefined) and not(triangle.C == undefined)

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
        elif NoSideDefined(triangle, undefined) and not NoAngleDefined(triangle, undefined):
            # no sides
                # has at least 1 angle
                if AllAnglesDefined(triangle, undefined):
                    # has all three angles and no sides *** Done ***
                    return triangle
                else:
                    # only 1 or 2 angles
                    if not (A == undefined):
                        # has angle A
                        if not (B == undefined):
                            # has angle A and B but not angle C
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
                        elif not (C == undefined):
                            # has angle A and C but not angle B
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
                        else:
                            # only has angle A and no sides *** Done ***
                            return triangle
                    elif not (B == undefined):
                        # has angle B
                        if not (C == undefined):
                            # has angle B and C but not angle A
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
                        else:
                            # only has angle B and no sides *** Done ***
                            return triangle
                    else:
                        # only has angle C and no sides *** Done ***
                        return triangle
        if NoSideDefined(triangle, undefined):
        else:
            # at least 1 side
            if NoAngleDefined(triangle, undefined):
                # only Sides
                if AllSidesDefined(triangle, undefined):
                    # has all three sides
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
                else:
                    # only 1 or 2 sides and no angles *** Done ***
                    return triangle
            else:
                # has at least 1 angle and at least 1 side
                if AllSidesDefined(triangle, undefined):
                    # has at least 1 angle and all three sides
                    if AllAnglesDefined(triangle, undefined):
                        # has all 3 angles and all three sides *** Done ***
                        return triangle
                    else:
                        # has at least 1 angle and all three sides but not all angles
                        if A == undefined:
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
                        if B == undefined:
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
                        if C == undefined:
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
                else:
                    # has at least 1 angle and at least 1 side but not all sides
                    if AllAnglesDefined(triangle, undefined):
                        # has all three angles and at least 1 side but not all sides
                        if not (a == undefined) and not (b == undefined):
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
                        elif not (a == undefined) and not (c == undefined):
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
                        elif not (b == undefined) and not (c == undefined):
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
                        elif not (a == undefined):
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
                        elif not (b == undefined):
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
                        else:
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
                    else:
                        # has at least 1 angle and at least 1 side but not all sides or angles
                        if not (a == undefined) and not (b == undefined):
                            # have at least 1 angle and side a and side b
                            if not (A == undefined) and not (B == undefined):
                                # have angle A and angle B and side a and side b
                                continueHere()
                                return triangle
                            elif not (A == undefined) and not (C == undefined):
                                # have angle A and angle C and side a and side b
                                continueHere()
                                return triangle
                            elif not (B == undefined) and not (C == undefined):
                                # have angle B and angle C and side a and side b
                                continueHere()
                                return triangle
                            elif not (A == undefined):
                                # have angle A and side a and side b
                                continueHere()
                                return triangle
                            elif not (B == undefined):
                                # have angle B and side a and side b
                                continueHere()
                                return triangle
                            else:
                                # have angle C and side a and side b
                                continueHere()
                                return triangle
                        elif not (a == undefined) and not (c == undefined):
                            # have at least 1 angle and side a and side c
                            if not (A == undefined) and not (B == undefined):
                                # have angle A and angle B and side a and side c
                                continueHere()
                                return triangle
                            elif not (A == undefined) and not (C == undefined):
                                # have angle A and angle C and side a and side c
                                continueHere()
                                return triangle
                            elif not (B == undefined) and not (C == undefined):
                                # have angle B and angle C and side a and side c
                                continueHere()
                                return triangle
                            elif not (A == undefined):
                                # have angle A and side a and side c
                                continueHere()
                                return triangle
                            elif not (B == undefined):
                                # have angle B and side a and side c
                                continueHere()
                                return triangle
                            else:
                                # have angle C and side a and side c
                                continueHere()
                                return triangle
                        elif not (b == undefined) and not (c == undefined):
                            # have at least 1 angle and side b and side c
                            if not (A == undefined) and not (B == undefined):
                                # have angle A and angle B and side b and side c
                                continueHere()
                                return triangle
                            elif not (A == undefined) and not (C == undefined):
                                # have angle A and angle C and side b and side c
                                continueHere()
                                return triangle
                            elif not (B == undefined) and not (C == undefined):
                                # have angle B and angle C and side b and side c
                                continueHere()
                                return triangle
                            elif not (A == undefined):
                                # have angle A and side b and side c
                                continueHere()
                                return triangle
                            elif not (B == undefined):
                                # have angle B and side b and side c
                                continueHere()
                                return triangle
                            else:
                                # have angle C and side b and side c
                                continueHere()
                                return triangle
                        elif not (a == undefined):
                            # have at least 1 angle and only side a
                            if not (A == undefined) and not (B == undefined):
                                # have angle A and angle B and side a
                                continueHere()
                                return triangle
                            elif not (A == undefined) and not (C == undefined):
                                # have angle A and angle C and side a
                                continueHere()
                                return triangle
                            elif not (B == undefined) and not (C == undefined):
                                # have angle B and angle C and side a
                                continueHere()
                                return triangle
                            elif not (A == undefined):
                                # have angle A and side a *** Done ***
                                return triangle
                            elif not (B == undefined):
                                # have angle B and side a *** Done ***
                                return triangle
                            else:
                                # have angle C and side a *** Done ***
                                return triangle
                        elif not (b == undefined):
                            # have at least 1 angle and only side b
                            if not (A == undefined) and not (B == undefined):
                                # have angle A and angle B and side b
                                continueHere()
                                return triangle
                            elif not (A == undefined) and not (C == undefined):
                                # have angle A and angle C and side b
                                continueHere()
                                return triangle
                            elif not (B == undefined) and not (C == undefined):
                                # have angle B and angle C and side b
                                continueHere()
                                return triangle
                            elif not (A == undefined):
                                # have angle A and side b *** Done ***
                                return triangle
                            elif not (B == undefined):
                                # have angle B and side b *** Done ***
                                return triangle
                            else:
                                # have angle C and side b *** Done ***
                                return triangle
                        else:
                            # have at least 1 angle and only side c
                            if not (A == undefined) and not (B == undefined):
                                # have angle A and angle B and side c
                                continueHere()
                                return triangle
                            elif not (A == undefined) and not (C == undefined):
                                # have angle A and angle C and side c
                                continueHere()
                                return triangle
                            elif not (B == undefined) and not (C == undefined):
                                # have angle B and angle C and side c
                                continueHere()
                                return triangle
                            elif not (A == undefined):
                                # have angle A and side c *** Done ***
                                return triangle
                            elif not (B == undefined):
                                # have angle B and side c *** Done ***
                                return triangle
                            else:
                                # have angle C and side c *** Done ***
                                return triangle
    else:
        raise TriangleError(f"object is not a Triangle!  type={type(triangle)}")

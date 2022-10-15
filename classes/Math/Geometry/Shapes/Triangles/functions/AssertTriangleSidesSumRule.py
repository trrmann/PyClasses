# AssertTriangleSidesSumRule.py
from Classes.Math.Geometry.Shapes.Triangles.errors.TriangleError import TriangleError
from Classes.Math.Geometry.Shapes.Triangles.functions.TriangleSidesSumRule import TriangleSidesSumRule
from Classes.Math.Geometry.errors.MissingDimensionError import MissingDimensionError

"""
Sum of the length of any two sides of a triangle is always greater than the third side
"""

def AssertTriangleSidesSumRule(a: float, b: float, c: float):
    try:
        if not TriangleSidesSumRule("a", float(a), float(b), float(c)):
            raise TriangleError(f"a: {a} + b: {b} + c: {c} == a({a}) !< b+c({b + c})")
        elif not TriangleSidesSumRule("b", float(a), float(b), float(c)):
            raise TriangleError(f"a: {a} + b: {b} + c: {c} == b({b}) !< a+c({a + c})")
        elif not TriangleSidesSumRule("b", float(a), float(b), float(c)):
            raise TriangleError(f"a: {a} + b: {b} + c: {c} == c({c}) !< a+b({a + b})")
        else:
            return True
    except ValueError:
        try:
            float(a)
            try:
                float(b)
                raise MissingDimensionError(f"Missing the side c for the triangle!", "triangle", "c")
            except ValueError:
                raise MissingDimensionError(f"Missing the side b for the triangle!", "triangle", "b")
        except ValueError:
            raise MissingDimensionError(f"Missing the side a for the triangle!", "triangle", "a")

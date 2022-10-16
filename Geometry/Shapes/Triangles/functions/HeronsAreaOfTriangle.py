# HeronsAreaOfTriangle.py
import Classes.Math.Geometry.Shapes.Triangles.functions.SemiPerimeterOfTriangle as SemiPerimeterOfTriangle
import Classes.Math.Geometry.errors.MissingDimensionError as MissingDimensionError
import math

"""
By Heron’s formula, the area of the triangle is given by:
          A = √[s(s – a)(s – b)(s – c)]
"""

def HeronsAreaOfTriangle(a: float, b: float, c: float):
    try:
        s = SemiPerimeterOfTriangle(float(a), float(b), float(c))
        return math.sqrt(s * (s - a) * (s -b) * (s - c))
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

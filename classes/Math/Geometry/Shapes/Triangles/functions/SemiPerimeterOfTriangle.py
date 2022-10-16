# SemiperimeterOfTriangle.py
import Classes.Math.Geometry.Shapes.Triangles.functions.PerimeterOfTriangle as PerimeterOfTriangle
import Classes.Math.Geometry.errors.MissingDimensionError as MissingDimensionError

def SemiPerimeterOfTriangle(a: float, b: float, c: float):
    try:
        return PerimeterOfTriangle(float(a), float(b), float(c)) / 2
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

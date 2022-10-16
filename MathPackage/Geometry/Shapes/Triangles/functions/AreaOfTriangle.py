# AreaOfTriangle.py
import Classes.Math.Geometry.Shapes.Triangles.functions.AreaOfRightTriangle as AreaOfRightTriangle
import Classes.Math.Geometry.Shapes.Triangles.functions.BaseOfTriangle as BaseOfTriangle
import Classes.Math.Geometry.Shapes.Triangles.functions.HeightOfTriangle as HeightOfTriangle
import Classes.Math.Geometry.errors.MissingDimensionError as MissingDimensionError

def AreaOfTriangle(a: float, b: float, c: float):
    try:
        return AreaOfRightTriangle(BaseOfTriangle(float(a), float(b), float(c)), HeightOfTriangle(float(a), float(b), float(c)))
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

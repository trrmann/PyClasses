# AreaOfRightTriangle.py
import Classes.Math.Geometry.errors.MissingDimensionError as MissingDimensionError

def AreaOfRightTriangle(base: float, height: float):
    try:
        return float(base) * float(height) / 2
    except ValueError:
        try:
            float(base)
            raise MissingDimensionError(f"Missing the height dimension for the triangle!", "triangle", "height")
        except ValueError:
            raise MissingDimensionError(f"Missing the length of the base dimension for the triangle!", "triangle", "base")

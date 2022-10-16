# Geometry.py
import Classes.Math.Geometry.errors.GeometryError as GeometryError

class MissingDimensionError(GeometryError.GeometryError):
    """Raised when the item is unknown"""
    pass

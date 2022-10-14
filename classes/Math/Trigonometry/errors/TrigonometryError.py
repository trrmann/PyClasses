# TrigonometryError.py
from Classes.Math.Geometry.errors.GeometryError import GeometryError

class TrigonometryError(GeometryError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

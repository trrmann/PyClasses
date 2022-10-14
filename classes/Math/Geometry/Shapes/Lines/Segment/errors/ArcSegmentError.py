# ArcSegmentError.py
from Classes.Math.Geometry.Shapes.Lines.Segment.errors.LineSegmentError import LineSegmentError
from Classes.Math.Algebra.Lines.Segment.errors.ArcSegmentError import ArcSegmentError as AlgebraArcSegmentError

class ArcSegmentError(AlgebraArcSegmentError, LineSegmentError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

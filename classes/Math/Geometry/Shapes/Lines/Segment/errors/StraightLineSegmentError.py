# StraightLineSegmentError.py
from Classes.Math.Geometry.Shapes.Lines.Segment.errors.LineSegmentError import LineSegmentError
from Classes.Math.Algebra.Lines.Segment.errors.StraightLineSegmentError import StraightLineSegmentError as AlgebraStraightLineSegmentError

class StraightLineSegmentError(AlgebraStraightLineSegmentError, LineSegmentError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

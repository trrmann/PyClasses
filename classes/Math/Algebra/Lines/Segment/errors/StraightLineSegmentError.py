# StraightLineSegmentError.py
import Classes.Math.Algebra.Lines.Segment.errors.LineSegmentError as LineSegmentError
import Classes.Math.Algebra.Lines.errors.StraightLineError as StraightLineError

class StraightLineSegmentError(StraightLineError.StraightLineError, LineSegmentError.LineSegmentError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

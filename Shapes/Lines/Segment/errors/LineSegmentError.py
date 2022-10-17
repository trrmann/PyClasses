# LineSegment.py
import Classes.Math.Geometry.Shapes.Lines.errors.LineError as LineError
import Classes.Math.Algebra.Lines.Segment.errors.LineSegmentError as AlgebraLineSegmentError

class LineSegmentError(LineError.LineError, AlgebraLineSegmentError.LineSegmentError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

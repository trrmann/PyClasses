# StraightLineSegmentError.py
from LineSegmentsPackage.LineSegmentErrorModule import LineSegmentError
from LinesPackage.StraightLineErrorModule import StraightLineError

class StraightLineSegmentError(StraightLineError, LineSegmentError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

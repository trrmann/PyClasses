# ArcSegmentError.py
from LineSegmentsPackage.LineSegmentErrorModule import LineSegmentError
from LinesPackage.ArcErrorModule import ArcError

class ArcSegmentError(ArcError, LineSegmentError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

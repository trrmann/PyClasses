# ArcSegment.py
from Classes.Math.Algebra.Lines.Segment.LineSegment import LineSegment, LineSegmentError
from Classes.Math.Algebra.Lines.Arc import Arc, ArcError

class ArcSegmentError(ArcError, LineSegmentError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class ArcSegment(Arc, LineSegment):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList,
            startCoordinate,
            endCoordinate,
            className = "ArcSegment"
        ):
        super().__init__(self, coordinatesList = coordinatesList, className = className)
        self.startCoordinate = startCoordinate
        self.endCoordinate = endCoordinate

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList}, startCoordinate={self.startCoordinate}, endCoordinate={self.endCoordinate})"
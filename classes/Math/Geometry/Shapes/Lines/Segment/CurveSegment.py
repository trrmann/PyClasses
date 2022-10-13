# CurveSegment.py
from Classes.Math.Geometry.Shapes.Lines.Segment.LineSegment import LineSegment, LineSegmentError
from Classes.Math.Algebra.Lines.Segment.CurveSegment import CurveSegment as AlgebraCurveSegment, CurveSegmentError as AlgebraCurveSegmentError

class CurveSegmentError(AlgebraCurveSegmentError, LineSegmentError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class CurveSegment(AlgebraCurveSegment, LineSegment):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList,
            startCoordinate,
            endCoordinate,
            className = "CurveSegment"
        ):
        super().__init__(self, coordinatesList = coordinatesList, className = className)
        self.startCoordinate = startCoordinate
        self.endCoordinate = endCoordinate

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList}, startCoordinate={self.startCoordinate}, endCoordinate={self.endCoordinate})"
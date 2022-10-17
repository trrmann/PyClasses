# StraightLineSegment.py
from LineSegmentsPackage.LineSegmentModule import LineSegment
from LinesPackage.StraightLineModule import StraightLine

class StraightLineSegment(StraightLine, LineSegment):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList,
            startCoordinate,
            endCoordinate,
            className = "StraightLineSegment"
        ):
        super().__init__(self, coordinatesList = coordinatesList, className = className)
        self.slope = 1
        self.yIntercept = 0
        self.startCoordinate = startCoordinate
        self.endCoordinate = endCoordinate

    def __init__(self,
            slope,
            yIntercept,
            startCoordinate,
            endCoordinate,
            className = "StraightLineSegment"
        ):
        super().__init__(self, coordinatesList = [yIntercept,0], className = className)
        self.slope = slope
        self.yIntercept = yIntercept
        self.startCoordinate = startCoordinate
        self.endCoordinate = endCoordinate

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList}, slope={self.slope}, y intercept={self.yIntercept}, startCoordinate={self.startCoordinate}, endCoordinate={self.endCoordinate})"

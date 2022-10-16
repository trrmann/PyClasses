# LineSegment.py
import Classes.Math.Algebra.Lines.Line as Line

class LineSegment(Line.Line):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList,
            startCoordinate,
            endCoordinate,
            className = "LineSegment"
        ):
        super().__init__(self, coordinatesList = coordinatesList, className = className)
        self.startCoordinate = startCoordinate
        self.endCoordinate = endCoordinate

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList}, startCoordinate={self.startCoordinate}, endCoordinate={self.endCoordinate})"

# LineSegment.py
import Classes.Math.Geometry.Shapes.Lines.Line as Line
import Classes.Math.Algebra.Lines.Segment.LineSegment as AlgebraLineSegment

class LineSegment(Line.Line, AlgebraLineSegment.LineSegment):
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

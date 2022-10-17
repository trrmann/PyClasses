# Line.py
import Classes.Math.Algebra.Lines.Line as AlgebraLine
import Classes.Math.Geometry.Shapes.Shape as Shape

class Line(Shape.Shape, AlgebraLine.Line):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, coordinatesList, className = "Line", classification="0 dimension", type="Line", dimensions=["coordinatesList"]):
        super().__init__(self, className = className)
        super().__init__(self, classification, type, dimensions, className = className)
        self.coordinatesList = coordinatesList

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, coordinatesList={self.coordinatesList})"
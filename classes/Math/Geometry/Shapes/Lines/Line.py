# Line.py
from Classes.Math.Algebra.Algebra import Algebra, AlgebraError
#from Classes.Math.Geometry.Shapes.Shape import Shape, ShapeError

#class LineError(ShapeError, AlgebraError):
class LineError(AlgebraError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

#class Line(Shape, Algebra):
class Line(Algebra):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

#    def __init__(self, coordinatesList, className = "Line", classification="0 dimension", type="Line", dimensions=["coordinatesList"]):
#        super().__init__(self, className = className)
#        super().__init__(self, classification, type, dimensions, className = className)
#        self.coordinatesList = coordinatesList
    def __init__(self,
            coordinatesList,
            className = "Line"
        ):
        super().__init__(self, className = className)
        self.coordinatesList = coordinatesList

#    def __repr__(self) -> str:
#        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, coordinatesList={self.coordinatesList})"
    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList})"

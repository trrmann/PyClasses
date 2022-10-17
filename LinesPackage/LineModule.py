# Line.py
from AlgebraPackage.AlgebraModule import Algebra
from ShapesPackage.ShapeModule import Shape

class Line(Algebra, Shape):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList,
            className = "Line"
        ):
        super().__init__(self, className = className)
        self.coordinatesList = coordinatesList

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList})"

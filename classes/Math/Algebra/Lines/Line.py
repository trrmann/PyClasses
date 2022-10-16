# Line.py
import Classes.Math.Algebra.Algebra as Algebra

class Line(Algebra.Algebra):
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

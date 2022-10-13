# Arc.py
from Classes.Math.Geometry.Shapes.Lines.Line import Line, LineError
from Classes.Math.Algebra.Lines.Arc import Arc as AlgebraArc, ArcError as AlgebraArcError

class ArcError(LineError, AlgebraArcError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Arc(Line, AlgebraArc):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList,
            className = "Arc"
        ):
        super().__init__(self, coordinatesList = coordinatesList, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList})"

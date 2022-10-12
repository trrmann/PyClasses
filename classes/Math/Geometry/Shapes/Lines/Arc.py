# Arc.py
from Classes.Math.Algebra.Lines.Line import Line, LineError

class ArcError(LineError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Arc(Line):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList,
            className = "Arc"
        ):
        super().__init__(self, coordinatesList = coordinatesList, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList})"

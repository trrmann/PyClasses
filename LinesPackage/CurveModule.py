# Curve.py
from LinesPackage.LineModule import Line

class Curve(Line):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList,
            className = "Curve"
        ):
        super().__init__(self, coordinatesList = coordinatesList, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList})"

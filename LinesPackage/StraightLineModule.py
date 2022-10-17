# Straight.py
from LinesPackage.LineModule import Line

class StraightLine(Line):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinatesList = [0,0],
            className = "Straight"
        ):
        super().__init__(self, coordinatesList = coordinatesList, className = className)
        self.slope = 1
        self.yIntercept = 0

    def __init__(self,
            slope,
            yIntercept,
            className = "Straight"
        ):
        super().__init__(self, coordinatesList = [yIntercept,0], className = className)
        self.slope = slope
        self.yIntercept = yIntercept

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinatesList={self.coordinatesList}, slope={self.slope}, y intercept={self.yIntercept})"

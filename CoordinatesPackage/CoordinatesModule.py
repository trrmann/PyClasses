# Coordinates.py
from AlgebraPackage.AlgebraModule import Algebra

class Coordinates(Algebra):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            className = "Coordinates"
        ):
        super().__init__(self, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"

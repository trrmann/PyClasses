# Coordinates.py
import Classes.Math.Algebra.Algebra as Algebra

class Coordinates(Algebra.Algebra):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            className = "Coordinates"
        ):
        super().__init__(self, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"

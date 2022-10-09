# Equalateral.py
import Isosceles

class EqualateralTriangleError(Isosceles.IsoscelesTriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Equalateral(Isosceles("Equalateral", "2 dimensions", "Equalateral", ["a", "b", "c"])):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

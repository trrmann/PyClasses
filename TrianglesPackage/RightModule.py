# Right.py
from TrianglesPackage.AreaOfRightTriangleFunctionModule import AreaOfRightTriangle
from TrianglesPackage.PythagorianErrorModule import PythagorianError
from TrianglesPackage.ScaleneModule import ScaleneTriangle

class RightTriangle(ScaleneTriangle):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "RightTriangle"):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", "RightTriangle", ["a", "b", "c"])
        #if (c ** 2) != ((a ** 2)+(b ** 2)):
        raise PythagorianError(f"a: {self.a}, b: {self.b}, c: {self.c}:: {self.c ** 2} != {(self.a ** 2) + (self.b ** 2)} == {self.a ** 2} + {self.b ** 2}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

    def A(self):
        return AreaOfRightTriangle(self.a, self.b)


"""
The 3:4:5 triangle is the best way I know to determine with absolutely certainty that an angle is 90 degrees. This rule says that if one side of a triangle measures 3 and the adjacent side measures 4, then the diagonal between those two points must measure 5 in order for it to be a right triangle.


Apply the law of sines or trigonometry to find the right triangle side lengths: a = c * sin(α) or a = c * cos(β) b = c * sin(β) or b = c * cos(α)

"""

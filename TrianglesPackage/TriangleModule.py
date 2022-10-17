# Triangle.py
from ClassesPackage.InvalidParameterErrorModule import InvalidParameterError
from ShapesPackage.ShapeModule import Shape
from TrigonometryPackage.TrigonometryModule import Trigonometry
from TrianglesPackage.SolveTriangleFunctionModule import SolveTriangle
from TrianglesPackage.AssertTriangleFunctionModule import AssertTriangle
from TrianglesPackage.AngleFromSidesFunctionModule import AngleFromSides
from TrianglesPackage.AreaOfTriangleFunctionModule import AreaOfTriangle
from TrianglesPackage.PerimeterOfTriangleFunctionModule import PerimeterOfTriangle
from TrianglesPackage.SemiPerimeterOfTriangleFunctionModule import SemiPerimeterOfTriangle
from TrianglesPackage.BaseOfTriangleFunctionModule import BaseOfTriangle
from TrianglesPackage.HeightOfTriangleFunctionModule import HeightOfTriangle
from TrianglesPackage.LengthOfMedianFunctionModule import LengthOfMedian
from TrianglesPackage.InradiusOfTriangleFunctionModule import InradiusOfTriangle
from TrianglesPackage.CircumradiusOfTriangleFunctionModule import CircumradiusOfTriangle

"""
A triangle is a closed polygon in a two-dimensional plane having three sides and three angles. By the name itself, a triangle is made by combining two words tri means three and angle.

The five major properties of a triangle are:
It has three sides, three vertices and three angles.
Sum of all three angles equal to 180 degrees
Sum of the length of any two sides of a triangle is always greater than the third side
Perimeter of the triangle is equal to the sum of all three sides
Area of triangle is equal to half of the product of base and height
"""
__className = "Triangle"
__undefined = "undefined"
class Triangle(ClosedPolygon, Trigonometry):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(
            self,
            a: float = __undefined,
            b: float = __undefined,
            c: float = __undefined,
            A: float = __undefined,
            B: float = __undefined,
            C: float = __undefined,
            solveTriangle: bool =True,
            assertTriangle: bool = True,
            className = __className
        ):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", __className, ["a", "b", "c"])
        __asserted__ = False
        __solved__ = False
        self.a = a
        self.b = b
        self.c = c
        self.A = A
        self.B = B
        self.C = C
        try:
            if bool(solveTriangle):
                Triangle.solve(self)
                __solved__ = True
        except ValueError:
            raise InvalidParameterError(f"Invalid Parameter Value!  solveTriangle needs to be True or False", "__init__ class Triangle", "solveTriangle")
        try:
            if bool(assertTriangle):
                assertTriangle(self)
                __asserted__ = True
        except ValueError:
            raise InvalidParameterError(f"Invalid Parameter Value!  assertTriangle needs to be True or False", "__init__ class Triangle", "assertTriangle")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c}, A={self.A}, B={self.B}, C={self.C})"

    def solve(self):
        return SolveTriangle(self, __undefined)

    def assertTriangle(self):
        AssertTriangle(self)

    def angle_A(self):
        return AngleFromSides("A", self.a, self.b, self.c)

    def angle_B(self):
        return AngleFromSides("B", self.a, self.b, self.c)

    def angle_C(self):
        return AngleFromSides("C", self.a, self.b, self.c)

    def A(self):
        return AreaOfTriangle(self.a, self.b, self.c)

    def P(self):
        return PerimeterOfTriangle(self.a, self.b, self.c)

    def s(self):
        return SemiPerimeterOfTriangle(self.a, self.b, self.c)

    def base(self):
        return BaseOfTriangle(self.a, self.b, self.c)

    def height(self):
        return HeightOfTriangle(self.a, self.b, self.c)

    def median_a(self):
        return LengthOfMedian("a", self.a, self.b, self.c)

    def median_b(self):
        return LengthOfMedian("b", self.a, self.b, self.c)

    def median_c(self):
        return LengthOfMedian("c", self.a, self.b, self.c)

    def inradius(self):
        return InradiusOfTriangle(self.a, self.b, self.c)

    def circumradius(self):
        return CircumradiusOfTriangle(self.a, self.b, self.c)

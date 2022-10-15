# Triangle.py
from Classes.Math.Geometry.Shapes.Triangles.functions.AssertTriangle import AssertTriangle
from Classes.Math.Geometry.Shapes.Triangles.functions.SolveTriangle import SolveTriangle
from Classes.errors.InvalidParameterError import InvalidParameterError
from Classes.Math.Geometry.Shapes.Shape import Shape
from Classes.Math.Geometry.Shapes.Triangles.functions.AngleFromSides import AngleFromSides
from Classes.Math.Geometry.Shapes.Triangles.functions.AssertAnglesFormTriangle import AssertAnglesFormTriangle
from Classes.Math.Geometry.Shapes.Triangles.functions.AreaOfTriangle import AreaOfTriangle
from Classes.Math.Geometry.Shapes.Triangles.functions.AssertTriangleSidesSumRule import AssertTriangleSidesSumRule
from Classes.Math.Geometry.Shapes.Triangles.functions.BaseOfTriangle import BaseOfTriangle
from Classes.Math.Geometry.Shapes.Triangles.functions.CircumradiusOfTriangle import CircumradiusOfTriangle
from Classes.Math.Geometry.Shapes.Triangles.functions.HeightOfTriangle import HeightOfTriangle
from Classes.Math.Geometry.Shapes.Triangles.functions.InradiusOfTriangle import InradiusOfTriangle
from Classes.Math.Geometry.Shapes.Triangles.functions.LengthOfMedian import LengthOfMedian
from Classes.Math.Geometry.Shapes.Triangles.functions.PerimeterOfTriangle import PerimeterOfTriangle
from Classes.Math.Geometry.Shapes.Triangles.functions.SemiPerimeterOfTriangle import SemiPerimeterOfTriangle

"""
A triangle is a closed polygon in a two-dimensional plane having three sides and three angles. By the name itself, a triangle is made by combining two words tri means three and angle.

The five major properties of a triangle are:
It has three sides, three vertices and three angles.
X Sum of all three angles equal to 180 degrees
X Sum of the length of any two sides of a triangle is always greater than the third side
X Perimeter of the triangle is equal to the sum of all three sides
X Area of triangle is equal to half of the product of base and height

"""
__className = "Triangle"
__undefined = "undefined"
class Triangle(Shape):
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

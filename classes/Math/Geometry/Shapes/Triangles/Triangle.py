# Triangle.py
from Classes.Math.Geometry.Shapes.Shape import Shape, ShapeError
import math

from Classes.Math.Geometry.Geometry import MissingDimension, A_right_triangle

class TriangleError(ShapeError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class PythagorianError(TriangleError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Triangle(Shape):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, a, b, c, className = "Triangle"):
        super().__init__(self, className)
        super().__init__(self, className, "2 dimensions", "Triangle", ["a", "b", "c"])
        self.a = a
        self.b = b
        self.c = c
        if (180) != (Triangle.angle_A() + Triangle.angle_B() + Triangle.angle_C()):
            raise TriangleError(f"<a: {Triangle.angle_A()} + <b: {Triangle.angle_B()} + <c: {Triangle.angle_C()} == {Triangle.angle_A()+Triangle.angle_B()+Triangle.angle_C()} != 180 degrees")
        #may be only for right triangles???? -- may need to use the 180 degrees rules instead
        #if (c ** 2) != ((a ** 2)+(b ** 2)):
        #    raise PythagorianError(f"a: {a}, b: {b}, c: {c}:: {c ** 2} != {(a ** 2) + (b ** 2)} == {a ** 2} + {b ** 2}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, classification={self.classification}, type={self.type}, dimensions={self.dimensions}, a={self.a}, b={self.b}, c={self.c})"

    def angle_A():
        try:
            return math.asin((float(Triangle.c) / math.sin(math.radians(Triangle.angle_C()))) / float(Triangle.a))
        except ValueError:
            try:
                float(Triangle.a)
                raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def angle_B():
        try:
            return math.asin((float(Triangle.c) / math.sin(math.radians(Triangle.angle_C()))) / float(Triangle.b))
        except ValueError:
            try:
                float(Triangle.b)
                raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
            except ValueError:
                raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")

    def angle_C():
        try:
            return math.degrees(math.acos(((float(Triangle.a) ** 2)+(float(Triangle.b) ** 2)-(float(Triangle.c) ** 2)) / (2 * float(Triangle.a) * float(Triangle.b))))
        except ValueError:
            try:
                float(Triangle.a)
                try:
                    float(Triangle.b)
                    raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
                except ValueError:
                    raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def A():
        return A_right_triangle(Triangle.base(), Triangle.height())

    def P():
        try:
            return float(Triangle.a) + float(Triangle.b) + float(Triangle.c)
        except ValueError:
            try:
                float(Triangle.a)
                try:
                    float(Triangle.b)
                    raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
                except ValueError:
                    raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def semiperimeter():
        try:
            return (float(Triangle.a) + float(Triangle.b) + float(Triangle.c)) / 2
        except ValueError:
            try:
                float(Triangle.a)
                try:
                    float(Triangle.b)
                    raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
                except ValueError:
                    raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def base():
        try:
            return float(Triangle.a)
        except ValueError:
            raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def height():
        try:
            return (2 / float(Triangle.a)) * math.sqrt(Triangle.semiperimeter() * (Triangle.semiperimeter() - float(Triangle.a)) * (Triangle.semiperimeter() - float(Triangle.b)) * (Triangle.semiperimeter() - float(Triangle.c)))
        except ValueError:
            try:
                float(Triangle.a)
                try:
                    float(Triangle.b)
                    raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
                except ValueError:
                    raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def median_a():
        try:
            return math.sqrt(((2 * (float(Triangle.b) ** 2))+(2 * (float(Triangle.c) ** 2))-(float(Triangle.a) ** 2))/4)
        except ValueError:
            try:
                float(Triangle.a)
                try:
                    float(Triangle.b)
                    raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
                except ValueError:
                    raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def median_b():
        try:
            return math.sqrt(((2 * (float(Triangle.a) ** 2))+(2 * (float(Triangle.c) ** 2))-(float(Triangle.b) ** 2))/4)
        except ValueError:
            try:
                float(Triangle.a)
                try:
                    float(Triangle.b)
                    raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
                except ValueError:
                    raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def median_c():
        try:
            return math.sqrt(((2 * (float(Triangle.a) ** 2))+(2 * (float(Triangle.b) ** 2))-(float(Triangle.c) ** 2))/4)
        except ValueError:
            try:
                float(Triangle.a)
                try:
                    float(Triangle.b)
                    raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
                except ValueError:
                    raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def inradius():
        try:
            return Triangle.A() / ((float(Triangle.a) + float(Triangle.b) + float(Triangle.c)) / 2)
        except ValueError:
            try:
                float(Triangle.a)
                try:
                    float(Triangle.b)
                    raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
                except ValueError:
                    raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")

    def circumradius():
        try:
            return float(Triangle.a) / 2 * math.sin(math.acos(((float(Triangle.b) ** 2)+(float(Triangle.c) ** 2)-(float(Triangle.a) ** 2)) / 2 * float(Triangle.b) * float(Triangle.c)))
        except ValueError:
            try:
                float(Triangle.a)
                try:
                    float(Triangle.b)
                    raise MissingDimension(f"Missing the side c length dimension for the triangle!", "triangle", "c")
                except ValueError:
                    raise MissingDimension(f"Missing the side b length dimension for the triangle!", "triangle", "b")
            except ValueError:
                raise MissingDimension(f"Missing the side a length dimension for the triangle!", "triangle", "a")


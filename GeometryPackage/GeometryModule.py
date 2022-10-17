# Geometry.py
from AlgebraPackage.AlgebraModule import Algebra
from MissingDimensionErrorModule import MissingDimensionError
from UndefinedShapeErrorModule import UndefinedShapeError
from UndefinedOrientationErrorModule import UndefinedOrientationError
from ClassesPackage.InputFunctionModule import *

import math

class Geometry(Algebra):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Geometry"):
        super().__init__(className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"

#r = radius of the circle
def A_circle(r):
    try:
        return math.pi * float(r) ** 2
    except ValueError:
        raise MissingDimensionError(f"Missing the r dimension for a circle!", "circle", "r")

#major = radius of the major axis
#minor = radius of the minor axis
def A_ellipse(major, minor):
    try:
        return math.pi * float(major) * float(minor)
    except ValueError:
        try:
            float(major)
            raise MissingDimensionError(f"Missing the major dimension for the ellipse!", "ellipse", "major")
        except ValueError:
            raise MissingDimensionError(f"Missing the minor dimension for the ellipse!", "ellipse", "minor")

#l = length of one side of a square
def A_square(l):
    try:
        return float(l) ** 2
    except ValueError:
        raise MissingDimensionError(f"Missing the l dimension for a square!", "square", "l")

#l = length of the rectangle
#w = width of the rectangle
def A_rectangle(l, w):
    try:
        return float(l) * float(w)
    except ValueError:
        try:
            float(l)
            raise MissingDimensionError(f"Missing the w dimension for a rectangle!", "rectangle", "w")
        except ValueError:
            raise MissingDimensionError(f"Missing the l dimension for a rectangle!", "rectangle", "l")

def xSec_A_cone(dimensions):
    required_dimensions = ["b", "h"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a cone!", "cone", dimension)
    return Geometry.A_triangle(dimensions["b"], dimensions["h"])

def xSec_A_cylinder(dimensions):
    required_dimensions = ["l", "w"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a cylinder!", "cylinder", dimension)
    return A_rectangle(dimensions["l"], dimensions["w"])

def xSec_A_sphere(dimensions):
    required_dimensions = ["r"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a sphere!", "sphere", dimension)
    return A_circle(dimensions["r"])

def xSec_A_cube(dimensions):
    required_dimensions = ["l"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a cube!", "cube", dimension)
    return A_square(dimensions["l"])

def xSec_A_cuboid(dimensions):
    required_dimensions = ["l", "w"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a cuboid!", "cuboid", dimension)
    return A_rectangle(dimensions["l"], dimensions["w"])

def xSec_A_tetrahedron(dimensions):
    required_dimensions = ["b", "h"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a tetrahedron!", "tetrahedron", dimension)
    return Geometry.A_triangle(dimensions["b"], dimensions["h"])

def xSec_A_triangular_prism(dimensions):
    required_dimensions = ["b", "h"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a triangular prism!", "triangular_prism", dimension)
    return Geometry.A_triangle(dimensions["b"], dimensions["h"])

def xSec_A_isosahedron(dimensions):
    required_dimensions = ["l"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a isosahedron!", "isosahedron", dimension)
    return A_square(dimensions["l"])

def xSec_A_torus(dimensions):
    required_dimensions = ["ro", "ri"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a torus!", "torus", dimension)
    return A_circle(dimensions["ro"])-A_circle(dimensions["ri"])

def xSec_A_hexagonal_prism(dimensions):
    required_dimensions = ["l"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a hexagonal_prism!", "hexagonal_prism", dimension)
    return A_square(dimensions["1"])

def xSec_A_octahedron(dimensions):
    required_dimensions = ["l"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a octahedron!", "octahedron", dimension)
    return A_square(dimensions["1"])

def xSec_A_ellipsoid(dimensions):
    required_dimensions = ["major", "minor"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a ellipsoid!", "ellipsoid", dimension)
    return A_ellipse(dimensions["major"], dimensions["minor"])

def xSec_A_pentagonal_prism(dimensions):
    required_dimensions = ["l"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a pentagonal_prism!", "pentagonal_prism", dimension)
    return A_square(dimensions["1"])

def xSec_A_pentagonal_pyramid(dimensions):
    required_dimensions = ["l"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a pentagonal_pyramid!", "pentagonal_pyramid", dimension)
    return A_square(dimensions["1"])

def xSec_A_hexagonal_pyramid(dimensions):
    required_dimensions = ["l"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a hexagonal_pyramid!", "hexagonal_pyramid", dimension)
    return A_square(dimensions["1"])

def xSec_A_octagonal_prism(dimensions):
    required_dimensions = ["l"]
    for dimension in required_dimensions:
        if dimension not in dimensions:
            raise MissingDimensionError(f"Missing the {dimension} dimension for a octagonal_prism!", "octagonal_prism", dimension)
    return A_square(dimensions["1"])

geometry_constants = {
    "shape" : {
        "point" : {
            "dimensions" : 0,
            "cartesian" : ["x", "y"],
            "threeDimensional" : ["x", "y", "z"],
            "fourDimensional" : ["x", "y", "z", "t"]
        },
        "straightLine" : {
            "dimensions" : 1,
            "cartesian" : [["cartesian point a", "cartesian point b"], ["m", "b"]],
            "threeDimensional" : [["threeDimensional point a", "threeDimensional point b"], ["mx", "my", "z-intercept"]],
            "fourDimensional" : [["fourDimensional point a", "fourDimensional point b"], ["mx", "my", "mz", "t-intercept"]]
        },
        "straightLineSegment" : {
            "dimensions" : 1,
            "cartesian" : [["cartesian start point", "cartesian end point"], ["cartesian start point", "m", "b", "l"]],
            "threeDimensional" : [["threeDimensional start point", "threeDimensional end point"], ["threeDimensional start point", "mx", "my", "z-intercept", "l"]],
            "fourDimensional" : [["fourDimensional start point", "fourDimensional end point"], ["fourDimensional start point", "mx", "my", "mz", "t-intercept", "l"]],
            "generic" : [["l"]]
        },
        "curveLine" : {
            "dimensions" : 1
        },
        "curveLineSegment" : {
            "dimensions" : 1
        },
        "arc" : {
            "dimensions" : 1
        },
        "arcSegment" : {
            "dimensions" : 1
        },
        "triangle" : {
            "dimensions" : 2,
            # a^2 + b^2 = c^2
            "generic" : [["side_a", "side_b", "side_c"]],
#            "P" : Triangle.P,
#            "A" : Triangle.A,
#            "medianA" : Triangle.median_a,
#            "medianB" : Triangle.median_b,
#            "medianC" : Triangle.median_c,
#            "inradius" : Triangle.inradius,
#            "circumradius" : Triangle.circumradius
        },
        "scaleneTriangle" : {
            "dimensions" : 2,
            "generic" : [
                ["side_a", "side_b", "side_c"]],
            "inherit" : [
                "triangle",
                [{
                    "side_a" : "side_a",
                    "side_b" : "side_b",
                    "side_c" : "side_c"}] ]
        },
        "isoscelesTriangle" : {
            "dimensions" : 2,
            # 2 <'s are equal and lengths of the sides opposite the equal angles are equal
            "generic" : [
                ["sides_ab", "side_c"]],
            "inherit" : [
                "scaleneTriangle",
                [{
                    "side_a" : "sides_ab",
                    "side_b" : "sides_ab",
                    "side_c" : "side_c"}] ]
        },
        "equilateralTriangle" : {
            "dimensions" : 2,
            # all <'s are 60deg
            "generic" : [
                ["l"]],
            "inherit" : [
                "isoscelesTriangle",
                [{
                    "sides_ab" : "l",
                    "side_c" : "l"}] ]
        },
        "acuteTriangle" : {
            "dimensions" : 2,
            # all 3 <'s less than 90deg
            # sum of all <'s = 180deg
            "generic" : [
                ["<a", "ol", "<b"],
                ["<a", "al", "<b"],
                ["<b", "ol", "<a"],
                ["<b", "al", "<a"],
                ["<", "al", "ol"]],
            "inherit" : [
                "scaleneTriangle",
                [{
                    "side_a" : "use <a, ol, and <b",
                    "side_b" : "use <a, ol, and <b",
                    "side_c" : "use <a, ol, and <b"},
                {
                    "side_a" : "use <a, al, and <b",
                    "side_b" : "use <a, al, and <b",
                    "side_c" : "use <a, al, and <b"},
                {
                    "side_a" : "use <b, ol, and <a",
                    "side_b" : "use <b, ol, and <a",
                    "side_c" : "use <b, ol, and <a"},
                {
                    "side_a" : "use <b, al, and <a",
                    "side_b" : "use <b, al, and <a",
                    "side_c" : "use <b, al, and <a"},
                {
                    "side_a" : "use <, al, and ol",
                    "side_b" : "use <, al, and ol",
                    "side_c" : "use <, al, and ol"}] ]
        },
        "obtuseTriangle" : {
            "dimensions" : 2,
            # 1 < greater than 90deg -- (major <)
            # sum of all <'s = 180deg
            "generic" : [
                ["major<", "ol", "minor<"],
                ["major<", "al", "o<"],
                ["major<", "al", "a<"],
                ["minor<", "ol", "major<"],
                ["minor<", "al", "major<"],
                ["minor<A", "minorAl", "minor<B"],
                ["minor<A", "majorAl", "minor<B"],
                ["minor<A", "ol", "minor<B"],
                ["major<", "al", "ol"],
                ["minor<", "minorAl", "ol"],
                ["minor<", "majorAl", "ol"]],
            "inherit" : [
                "scaleneTriangle",
                [{
                    "side_a" : "use major<, ol, and minor<",#(ol / sin(major<)) * sin(minor<)  -- a_from_major_angle_opposite_side_and_minor_angle
                    "side_b" : "use major<, ol, and minor<",#sqrt((ol ** 2) - ((ol / sin(major<)) * sin(minor<) ** 2))
                    "side_c" : "ol"},
                {
                    "side_a" : "al",
                    "side_b" : "use major<, al, and o<",#sqrt((((al / sin(o<)) * sin(major<)) ** 2) - (al ** 2))
                    "side_c" : "use major<, al, and o<"},#((al / sin(o<)) * sin(major<))
                {
                    "side_a" : "al",
                    "side_b" : "use major<, al, and a<",#sqrt(((al / sin(180 - (major< + a<)) * sin(major<)) ** 2) - (al ** 2))
                    "side_c" : "use major<, al, and a<"},#al / sin(180 - (major< + a<)) * sin(major<)
                {
                    "side_a" : "ol",
                    "side_b" : "use minor<, ol, major<",#sqrt(((ol / sin(minor<) * sin(major<))**2)-(al**2))
                    "side_c" : "use minor<, ol, major<"},#ol / sin(minor<) * sin(major<)
                {
                    "side_a" : "use minor<, al, major<",#(al / sin(180-(major<+minor<))) * sin(minor<)
                    "side_b" : "al",
                    "side_c" : "use minor<, al, major<"},#sqrt((((al / sin(180-(major<+minor<))) * sin(minor<)) ** 2)+(al ** 2))
                {
                    "side_a" : "use minor<A, minorAl, minor<B",#(minoral/sin(minor<B))*sin(minor<A)
                    "side_b" : "minorAl",
                    "side_c" : "use minor<A, minorAl, minor<B"},#sqrt((((minoral/sin(minor<B))*sin(minor<A))**2)+(minoral**2))
                {
                    "side_a" : "use minor<A, majorAl, minor<B",#(majoral/sin(180-(minor<A+minor<B)))*sin(minor<A)
                    "side_b" : "use minor<A, majorAl, minor<B",#sqrt((al**2)-(((majoral/sin(180-(minor<A+minor<B)))*sin(minor<A))**2))
                    "side_c" : "majorAl"},
                {
                    "side_a" : "ol",
                    "side_b" : "use minor<A, ol, minor<B",#(ol/sin(minor<A))*sin(minor<B)
                    "side_c" : "use minor<A, ol, minor<B"},#sqrt((ol**2)+(((ol/sin(minor<A))*sin(minor<B))**2))
                {
                    "side_a" : "al",
                    "side_b" : "use major<, al, and ol",#sqrt((ol**2)-(al**2))
                    "side_c" : "ol"},
                {
                    "side_a" : "ol",
                    "side_b" : "minorAl",
                    "side_c" : "use minor<, minorAl, and ol"},#sqrt((ol**2)+(al**2))
                {
                    "side_a" : "ol",
                    "side_b" : "use minor<, majorAl, and ol",#sqrt((al**2)-(ol**2))
                    "side_c" : "majorAl"}] ]
        },
        "right_triangle" : {
            "dimensions" : 2,
            # 1 < equal to 90deg
            # sum of all <'s = 180deg
            "generic" : [
                ["<", "hl"],
                ["<","al"],
                ["<","ol"],
                ["hl","ll"]],
            "inherit" : [
#                "scaleneTriangle",
#                [{
#                    "side_a" : a_from_angle_and_hypotenuse,
#                    "side_b" : b_from_angle_and_hypotenuse,
#                    "side_c" : "hl"},
#                {
#                    "side_a" : a_from_angle_and_adjacent_side,
#                    "side_b" : "al",
#                    "side_c" : hypotenuse_from_angle_and_adjacent_side},
#                {
#                    "side_a" : "ol",
#                    "side_b" : b_from_angle_and_opposite_side,
#                    "side_c" : hypotenuse_from_angle_and_opposite_side},
#                {
#                    "side_a" : "ll",
#                    "side_b" : b_from_leg_and_hypotenuse,
#                    "side_c" : "hl"}]
            ]
        },
        "rectangle" : {
            "dimensions" : 2,
            "generic" : [["l", "w"]],
#            "P" : P_rectangle,
            "A" : A_rectangle
        },
        "square" : {
            "dimensions" : 2,
            "generic" : [["l"]],
            "inherit" : ["rectangle", {"l" : "l", "w" : "l"} ]
        },
        "ellipse" : {
            "dimensions" : 2,
            "generic" : [["major", "minor"]]
        },
        "circle" : {
            "dimensions" : 2,
            "generic" : [["r"]],
            "inherit" : ["ellipse", {"major" : "r", "minor" : "r"} ]
        },
        "cone" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_cone
        },
        "cylinder" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_cylinder
        },
        "sphere" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_sphere
        },
        "cube" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_cube
        },
        "cuboid" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_cuboid
        },
        "tetrahedron" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_tetrahedron
        },
        "triangular_prism" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_triangular_prism
        },
        "isosahedron" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_isosahedron
        },
        "torus" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_torus
        },
        "hexagonal_prism" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_hexagonal_prism
        },
        "octahedron" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_octahedron
        },
        "ellipsoid" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_ellipsoid
        },
        "pentagonal_prism" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_pentagonal_prism
        },
        "pentagonal_pyramid" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_pentagonal_pyramid
        },
        "hexagonal_pyramid" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_hexagonal_pyramid
        },
        "octagonal_prism" : {
            "dimensions" : 3,
            "crossSectionalArea" : xSec_A_octagonal_prism
        }
    }
}

#Cross sectional area of the projectile shape
def A(shape, dimensions = {}):
    if shape.lower() in geometry_constants["shape"].keys():
        return geometry_constants["shape"][shape.lower()]["crossSectionalArea"](dimensions)
    else:
        raise UndefinedShapeError(f"Shape type {shape} is undefined in the constants dictionary!")

# Trigonometry.py
import math
from GeometryPackage.GeometryModule import Geometry

class Trigonometry(Geometry):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Trigonometry"):
        super().__init__(className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"

def a_from_angle_and_hypotenuse(dimensions):
    #"(hl/sin(90))*sin(<)"
    return float(dimensions["hl"]) / math.sin(math.radians(90)) * math.sin(math.radians(float(dimensions["<"])))

def b_from_angle_and_hypotenuse(dimensions):
    #"sqrt((hl**2)-((hl/sin(90))*sin(<)**2))"
    return math.sqrt((float(dimensions["hl"]) ** 2) - ((float(dimensions["hl"]) / math.sin(math.radians(90))) * math.sin(math.radians(float(dimensions["<"]))) ** 2))

def a_from_angle_and_adjacent_side(dimensions):
    #"(al/sin((90-<)))*sin(<)"
    return (float(dimensions["al"]) / math.sin(math.radians(90 - float(dimensions["<"])))) * math.sin(math.radians(float(dimensions["<"])))

def hypotenuse_from_angle_and_adjacent_side(dimensions):
    #"sqrt(((al/sin((90-<)))*sin(<)**2)+(al**2))"
    return math.sqrt(((float(dimensions["al"]) / math.sin(math.radians(90 - float(dimensions["<"])))) * math.sin(math.radians(float(dimensions["<"]))) ** 2) + (float(dimensions["al"]) ** 2))

def b_from_angle_and_opposite_side(dimensions):
    #"sqrt(((ol/sin(<))*sin(90)**2)-(ol**2))"
    return math.sqrt(((float(dimensions["ol"]) / math.sin(math.radians(float(dimensions["<"])))) * math.sin(math.radians(90)) ** 2) - (float(dimensions["ol"]) ** 2))

def hypotenuse_from_angle_and_opposite_side(dimensions):
    #"(ol/sin(<))*sin(90)"
    return (float(dimensions["ol"]) / math.sin(math.radians(float(dimensions["<"])))) * math.sin(math.radians(90))

def b_from_leg_and_hypotenuse(dimensions):
    #"math.sqrt((hl ** 2)-( ll ** 2))"
    return math.sqrt((float(dimensions["hl"]) ** 2) - (float(dimensions["ll"]) ** 2))


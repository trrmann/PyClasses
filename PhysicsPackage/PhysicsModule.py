# Physics.py
from EarthSciencePackage.EarthScienceModule import EarthScience
from ChemistryPackage.ChemistryModule import fluid_density
from EarthSciencePackage.EarthScienceModule import g
from GeometryPackage.UndefinedOrientationErrorModule import UndefinedOrientationError
from GeometryPackage.UndefinedShapeErrorModule import UndefinedShapeError
from GeometryPackage.GeometryModule import A
import math

physics_constants = {
    "shape" : {
        "cylinder" : {
            "drag_constant" : {
                "default" : "side",
                "side" : 1.1
            }
        },
        "sphere" : {
            "drag_constant" : {
                "default" : "all",
                "all" : .5
            }
        }
    }
}

class Physics(EarthScience):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Physics"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"

#Drag force constant
def C(shape, shape_orientation = "default"):
    if shape_orientation == "": shape_orientation = "default"
    if shape.lower() in physics_constants["shape"].keys():
        if shape_orientation.lower() in physics_constants["shape"][shape.lower()]["drag_constant"].keys():
            if type(physics_constants["shape"][shape.lower()]["drag_constant"][shape_orientation.lower()]) is float:
                return physics_constants["shape"][shape.lower()]["drag_constant"][shape_orientation.lower()]
            else:
                return C(shape, physics_constants["shape"][shape.lower()]["drag_constant"][shape_orientation.lower()])
        else:
            raise UndefinedOrientationError(f"The Drag force constant for shape type {shape} orientation {shape_orientation} is undefined in the constants dictionary!")
    else:
        raise UndefinedShapeError(f"Shape type {shape} is undefined in the constants dictionary!")

# speed of light
def c(type_of_fluid, shape, shape_dimensions = {}, shape_orientation = "default"):
    return 1 / 2 * fluid_density(type_of_fluid) * A(shape, shape_dimensions) * C(shape, shape_orientation)

# t = time in seconds
# m = mass in kg
def v(t, m, shape, shape_dimensions = {}, shape_orientation = "default", type_of_fluid = "air", location = "earth"):
    _c = c(type_of_fluid, shape, shape_dimensions, shape_orientation)
    return math.sqrt(m * g(location) / _c) * (1 - math.exp(-1 * math.sqrt(m * g(location) * _c) / m * t))

# Physics.py
from Classes.Science.EarthScience.EarthScience import EarthScience, EarthScienceError
import math

from Math import UndefinedOrientation, UndefinedShape, A

class PhysicsError(EarthScienceError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class UndefinedCelestialLocation(PhysicsError):
    """Raised when the item is unknown"""
    pass

class UndefinedFluidType(PhysicsError):
    """Raised when the item is unknown"""
    pass

class Physics(EarthScience):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Physics"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"


physics_constants = {
    "g" : {
        "earth" : 9.8,
        "jupiter" : 24
    },
    "fluidDensity" : {
        "air" : 1.3,
        "water" : 1000
    },
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

#Gravitational force constant
def g(location = "earth"):
    if location.lower() in physics_constants["g"].keys():
        return physics_constants["g"][location.lower()]
    else:
        raise UndefinedCelestialLocation(f"Gravitational force for celestial location {location} is undefined in the constants dictionary!")

def fluid_density(type = "air"):
    if type.lower() in physics_constants["fluidDensity"].keys():
        return physics_constants["fluidDensity"][type.lower()]
    else:
        raise UndefinedFluidType(f"Density for fluid type {type} is undefined in the constants dictionary!")

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
            raise UndefinedOrientation(f"The Drag force constant for shape type {shape} orientation {shape_orientation} is undefined in the constants dictionary!")
    else:
        raise UndefinedShape(f"Shape type {shape} is undefined in the constants dictionary!")

# speed of light
def c(type_of_fluid, shape, shape_dimensions = {}, shape_orientation = "default"):
    return 1 / 2 * fluid_density(type_of_fluid) * A(shape, shape_dimensions) * C(shape, shape_orientation)

# t = time in seconds
# m = mass in kg
def v(t, m, shape, shape_dimensions = {}, shape_orientation = "default", type_of_fluid = "air", location = "earth"):
    _c = c(type_of_fluid, shape, shape_dimensions, shape_orientation)
    return math.sqrt(m * g(location) / _c) * (1 - math.exp(-1 * math.sqrt(m * g(location) * _c) / m * t))


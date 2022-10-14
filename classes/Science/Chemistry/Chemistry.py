# Chemestry.py
from Classes.Science.Chemistry.errors.UndefinedFluidTypeError import UndefinedFluidTypeError
from Classes.Science.EarthScience.EarthScience import EarthScience

chemestry_constants = {
    "fluidDensity" : {
        "air" : 1.3,
        "water" : 1000
    }
}

class Chemestry(EarthScience):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Chemestry"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"

def fluid_density(type = "air"):
    if type.lower() in chemestry_constants["fluidDensity"].keys():
        return chemestry_constants["fluidDensity"][type.lower()]
    else:
        raise UndefinedFluidTypeError(f"Density for fluid type {type} is undefined in the constants dictionary!")

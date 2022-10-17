# Chemestry.py
import ClassesPackage.Science.Chemistry.errors.UndefinedFluidTypeError as UndefinedFluidTypeError
import ClassesPackage.Science.EarthScience.EarthScience as EarthScience

chemestry_constants = {
    "fluidDensity" : {
        "air" : 1.3,
        "water" : 1000
    }
}

class Chemestry(EarthScience.EarthScience):
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

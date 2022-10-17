# EarthScience.py
import ClassesPackage.Science.Science as Science
import ClassesPackage.Science.EarthScience.errors.UndefinedCelestialLocationError as UndefinedCelestialLocationError

astro_constants = {
    "g" : {
        "earth" : 9.8,
        "jupiter" : 24
    }
}

class EarthScience(Science.Science):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "EarthScience"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"

#Gravitational force constant
def g(location = "earth"):
    if location.lower() in astro_constants["g"].keys():
        return astro_constants["g"][location.lower()]
    else:
        raise UndefinedCelestialLocationError(f"Gravitational force for celestial location {location} is undefined in the constants dictionary!")

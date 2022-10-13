# EarthScience.py
from Classes.Science.Science import Science, ScienceError

class EarthScienceError(ScienceError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class EarthScience(Science):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "EarthScience"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"

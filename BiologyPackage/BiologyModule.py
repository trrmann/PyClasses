# Biology.py
import ClassesPackage.Science.EarthScience.EarthScience as EarthScience

class Biology(EarthScience.EarthScience):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Biology"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"

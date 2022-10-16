# Point.py
import Classes.Math.Algebra.Coordinates.Coordinates as Coordinates

class Point(Coordinates.Coordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            coordinates,
            className = "Point"
        ):
        super().__init__(self, className = className)
        self.coordinates = coordinates

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, coordinates={self.coordinates})"

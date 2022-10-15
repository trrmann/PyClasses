# OppositeSideFromSideSideInteriorAngle.py
from Classes.errors.InvalidParameterError import InvalidParameterError
import math

def OppositeSideFromSideSideInteriorAngle(AngleOppositeResultSide: float, FirstSideAdjacentGivenAngle: float, SecondSideAdjacentGivenAngle: float):
    try:
        return math.sqrt((float(FirstSideAdjacentGivenAngle) ** 2) + (float(SecondSideAdjacentGivenAngle) ** 2) - (2 * float(FirstSideAdjacentGivenAngle) * float(SecondSideAdjacentGivenAngle) * math.cos(math.radians(float(AngleOppositeResultSide)))))
    except ValueError:
        try:
            float(AngleOppositeResultSide)
            try:
                float(FirstSideAdjacentGivenAngle)
                raise InvalidParameterError(f"Invalid Parameter Value!  SecondSideAdjacentGivenAngle needs to be a float.  recieved({SecondSideAdjacentGivenAngle})", "OppositeSideFromSideSideInteriorAngle", "SecondSideAdjacentGivenAngle")
            except ValueError:
                raise InvalidParameterError(f"Invalid Parameter Value!  FirstSideAdjacentGivenAngle needs to be a float. recieved({FirstSideAdjacentGivenAngle})", "OppositeSideFromSideSideInteriorAngle", "FirstSideAdjacentGivenAngle")
        except ValueError:
            raise InvalidParameterError(f"Invalid Parameter Value!  AngleOppositeResultSide needs to be a float. recieved({AngleOppositeResultSide})", "OppositeSideFromSideSideInteriorAngle", "AngleOppositeResultSide")
# OppositeSideFromAngleAngleExteriorSide.py
import Classes.errors.InvalidParameterError as InvalidParameterError
import math

def OppositeSideFromAngleAngleExteriorSide(AngleOppositeResultSide: float, AngleOppositeGivenSide: float, ExteriorSide: float):
    try:
        return math.sin(math.radians(float(AngleOppositeResultSide))) * float(ExteriorSide) / math.sin(math.radians(float(AngleOppositeGivenSide)))
    except ValueError:
        try:
            float(AngleOppositeResultSide)
            try:
                float(AngleOppositeGivenSide)
                raise InvalidParameterError(f"Invalid Parameter Value!  ExteriorSide needs to be a float.  recieved({ExteriorSide})", "OppositeSideFromAngleAngleExteriorSide", "ExteriorSide")
            except ValueError:
                raise InvalidParameterError(f"Invalid Parameter Value!  AngleOppositeGivenSide needs to be a float. recieved({AngleOppositeGivenSide})", "OppositeSideFromAngleAngleExteriorSide", "AngleOppositeGivenSide")
        except ValueError:
            raise InvalidParameterError(f"Invalid Parameter Value!  AngleOppositeResultSide needs to be a float. recieved({AngleOppositeResultSide})", "OppositeSideFromAngleAngleExteriorSide", "AngleOppositeResultSide")
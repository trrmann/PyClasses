# OppositeAngleFromSideSideExteriorAngle.py
from Classes.errors.InvalidParameterError import InvalidParameterError
import math

def OppositeAngleFromSideSideExteriorAngle(SideOppositeResultAngle: float, SideOppositeGivenAngle: float, ExteriorAngle: float):
    try:
        return math.degrees(math.asin(math.radians(float(SideOppositeResultAngle)) * (math.sin(math.radians(float(ExteriorAngle))) / float(SideOppositeGivenAngle))))
    except ValueError:
        try:
            float(SideOppositeResultAngle)
            try:
                float(SideOppositeGivenAngle)
                raise InvalidParameterError(f"Invalid Parameter Value!  ExteriorAngle needs to be a float.  recieved({ExteriorAngle})", "OppositeAngleFromSideSideExteriorAngle", "ExteriorAngle")
            except ValueError:
                raise InvalidParameterError(f"Invalid Parameter Value!  SideOppositeGivenAngle needs to be a float. recieved({SideOppositeGivenAngle})", "OppositeAngleFromSideSideExteriorAngle", "SideOppositeGivenAngle")
        except ValueError:
            raise InvalidParameterError(f"Invalid Parameter Value!  SideOppositeResultAngle needs to be a float. recieved({SideOppositeResultAngle})", "OppositeAngleFromSideSideExteriorAngle", "SideOppositeResultAngle")
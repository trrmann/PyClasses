# NumberLine.py
from CoordinatesPackage.CoordinatesModule import Coordinates
from GridsPackage.InvalidMaximumErrorModule import InvalidMaximumError
from GridsPackage.InvalidMaximumLimitErrorModule import InvalidMaximumLimitError
from GridsPackage.InvalidMinimumErrorModule import InvalidMinimumError
from GridsPackage.InvalidMinimumLimitErrorModule import InvalidMinimumLimitError
from GridsPackage.InvalidOriginErrorModule import InvalidOriginError
from GridsPackage.InvalidValueErrorModule import InvalidValueError
from GridsPackage.ValueExceedsMaxiumErrorModule import ValueExceedsMaxiumError
from GridsPackage.ValueExceedsMaxiumLimitErrorModule import ValueExceedsMaxiumLimitError
from GridsPackage.ValueExceedsMinimumErrorModule import ValueExceedsMinimumError
from GridsPackage.ValueExceedsMinimumLimitErrorModule import ValueExceedsMinimumLimitError

class NumberLine(Coordinates):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            origin: float = 0.0,
            major_display_tick_period: float = 5,
            minor_display_tick_period: float = 1,
            min: float = "none",
            min_limit: bool = False,
            max: float = "none",
            max_limit: bool= False,
            period: float = "none",
            value: float=0.0,
            className = "NumberLine"
        ):
        super().__init__(self, className = className)
        self.origin(origin, True)
        self.major_display_tick_period(major_display_tick_period, True)
        self.minor_display_tick_period(minor_display_tick_period, True)
        self.min_limit(min_limit, True)
        self.min(min, True)
        self.max_limit(max_limit, True)
        self.max(max, True)
        self.period(period, True)
        self.value(value)

    def __repr__(self) -> str:
        if(self.__inf and self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.origin()}, -∞, ∞, value={self.value()})"
        elif(self.__inf):
            return f"{type(self).__name__}(className={self.className}, origin={self.origin()}, {self.min()}, ∞, value={self.value()})"
        elif(self.__negInf):
            return f"{type(self).__name__}(className={self.className}, origin={self.origin()}, -∞, {self.max()}, value={self.value()})"
        else:
            return f"{type(self).__name__}(className={self.className}, origin={self.origin()}, {self.min()}, {self.max()}, value={self.value()})"

    def origin(self, origin: float, init = False):
        try:
            if (not init) and (self.has_min()) and ((not self.min_limit()) and (float(origin) < self.min())):
                raise InvalidOriginError(f"Origin {origin} is less than the minimum {self.min()}!", self.min(), origin)
            if (not init) and (self.has_min()) and ((self.min_limit()) and (float(origin) <= self.min())):
                raise InvalidOriginError(f"Origin {origin} is less than or equal to the minimum limit {self.min()}!", self.min(), origin)
            elif (not init) and (self.has_max()) and ((not self.max_limit()) and (float(origin) > self.max())):
                raise InvalidOriginError(f"Origin {origin} is greater than the maximum {self.max()}!", self.max(), origin)
            elif (not init) and (self.has_max()) and ((self.max_limit()) and (float(origin) >= self.max())):
                raise InvalidOriginError(f"Origin {origin} is greater than or equal to the maximum limit {self.max()}!", self.max(), origin)
            elif (not init) and (self.is_cyclic()) and (float(int(float(origin) / self.period())) != 0.0):
                raise InvalidOriginError(f"Origin {origin} is not in the base revolution for a period of {self.period()}!", self.period(), origin)
            else:
                self.__origin = float(origin)
        except ValueError:
            raise InvalidOriginError(f"Unable to convert \"{origin}\" to float", origin)
    
    def origin(self):
        return self.__origin

    def major_display_tick_period(self, major_display_tick_period: float, init = False):
        self.__major_display_tick_period = float(major_display_tick_period)

    def major_display_tick_period(self):
        return self.__major_display_tick_period

    def minor_display_tick_period(self, minor_display_tick_period: float, init = False):
        self.__minor_display_tick_period = float(minor_display_tick_period)

    def minor_display_tick_period(self):
        return self.__minor_display_tick_period

    def min_limit(self, min_limit: bool, init = False):
        self.__min_limit = bool(min_limit)

    def min_limit(self):
        return self.__min_limit

    def min(self, min: float, init = False):
        try:
            if (not init) and (self.has_max()) and (((not self.min_limit()) and (not self.max_limit())) and (float(min) > self.max())):
                raise InvalidMinimumError(f"Minimum {min} is greater than the maximum {self.max()}!", self.max(), min)
            if (not init) and (self.has_max()) and (((self.min_limit()) or (self.max_limit())) and (float(min) >= self.max())):
                raise InvalidMinimumLimitError(f"Minimum (limit) {min} is greater than or equal to the maximum (limit) {self.max()}!", self.max(), min)
            elif (not init) and (((not self.min_limit())) and float(min) > self.full_value()):
                raise InvalidMinimumError(f"Minimum {min} is greater than the value {self.full_value()}!", self.full_value(), min)
            elif (not init) and ((self.min_limit()) and float(min) >= self.full_value()):
                raise InvalidMinimumLimitError(f"Minimum limit {min} is greater than or equal to the value {self.full_value()}!", self.full_value(), min)
            elif (not init) and (((not self.min_limit())) and float(min) > self.value()):
                raise InvalidMinimumError(f"Minimum {min} is greater than the value {self.value()}!", self.value(), min)
            elif (not init) and ((self.min_limit()) and float(min) >= self.value()):
                raise InvalidMinimumLimitError(f"Minimum limit {min} is greater than or equal to the value {self.value()}!", self.value(), min)
            elif (not self.min_limit()) and float(min) > self.origin():
                raise InvalidMinimumError(f"Minimum {min} is greater than the origin {self.origin()}!", self.origin(), min)
            elif (self.min_limit()) and float(min) >= self.origin():
                raise InvalidMinimumLimitError(f"Minimum limit {min} is greater than or equal to the origin {self.origin()}!", self.origin(), min)
            else:
                self.__min = float(min)
                self.__negInf = False
        except ValueError:
            self.__min = self.origin()
            self.__negInf = True
    
    def has_min(self) :
        return not self.__negInf

    def min(self):
        return self.__min

    def max_limit(self, max_limit: bool, init = False):
        self.__max_limit = bool(max_limit)

    def max_limit(self):
        return self.__max_limit

    def max(self, max: float, init = False):
        try:
            if (not init) and (self.has_min()) and (((not self.max_limit()) and (not self.min_limit())) and (float(max) < self.min())):
                raise InvalidMaximumError(f"Maxiumum {max} is less than the minimum {self.min()}!", self.min(), max)
            if (not init) and (self.has_min()) and (((self.max_limit()) or (self.min_limit())) and (float(max) <= self.min())):
                raise InvalidMaximumLimitError(f"Maxiumum (limit) {max} is less than or equal to the minimum (limit) {self.min()}!", self.min(), max)
            elif (not init) and ((not self.max_limit()) and (float(max) < self.full_value())):
                raise InvalidMaximumError(f"Maxiumum {max} is less than the value {self.full_value()}!", self.full_value(), max)
            elif (not init) and ((self.max_limit()) and (float(max) <= self.full_value())):
                raise InvalidMaximumLimitError(f"Maxiumum limit {max} is less than or equal to the value {self.full_value()}!", self.full_value(), max)
            elif (not init) and ((not self.max_limit()) and (float(max) < self.value())):
                raise InvalidMaximumError(f"Maxiumum {max} is less than the value {self.value()}!", self.value(), max)
            elif (not init) and ((self.max_limit()) and (float(max) <= self.value())):
                raise InvalidMaximumLimitError(f"Maxiumum limit {max} is less than or equal to the value {self.value()}!", self.value(), max)
            elif ((not self.max_limit()) and float(max) < self.origin()):
                raise InvalidMaximumError(f"Maxiumum {max} is less than the origin {self.origin()}!", self.origin(), max)
            elif ((self.max_limit()) and float(max) <= self.origin()):
                raise InvalidMaximumLimitError(f"Maxiumum limit {max} is less than or equal to the origin {self.origin()}!", self.origin(), max)
            else:
                self.__max = float(max)
                self.__inf = False
        except ValueError:
            self.__max = self.origin()
            self.__inf = True
    
    def has_max(self) :
        return not self.__inf

    def max(self):
        return self.__max

    def period(self, period: float, init = False):
        try:
            if float(period) != 0.0:
                self.__period = float(period)
                self.__cyclic = True
            else:
                self.__period = self.origin()
                self.__cyclic = False
        except ValueError:
            self.__period = self.origin()
            self.__cyclic = False

    def is_cyclic(self):
        return self.__cyclic == True

    def period(self):
        if self.is_cyclic():
            return self.__period
        else:
            return 1.0

    def value(self, value: float):
        try:
            if (self.has_min()) and ((not self.min_limit()) and (float(value) < self.min())):
                raise ValueExceedsMinimumError(f"value {value} exceeds the minimum {self.min()}!", self.min(), value)
            if (self.has_min()) and ((self.min_limit()) and (float(value) <= self.min())):
                raise ValueExceedsMinimumLimitError(f"value {value} exceeds or equals the minimum limit {self.min()}!", self.min(), value)
            elif (self.has_max()) and ((not self.max_limit()) and (float(value) > self.max())):
                raise ValueExceedsMaxiumError(f"value {value} exceeds the maximum {self.max()}!", self.max(), value)
            elif (self.has_max()) and ((self.max_limit()) and (float(value) >= self.max())):
                raise ValueExceedsMaxiumLimitError(f"value {value} exceeds or equals the maximum limit {self.max()}!", self.max(), value)
            else:
                self.__value = float(value)
        except ValueError:
            raise InvalidValueError(f"Unable to convert \"{value}\" to float", value)

    def full_value(self):
        return self.__value

    def value(self):
        return self.full_value() % self.period()

    def revolutions(self):
        if self.is_cyclic():
            return float(int(self.full_value() / self.period()))
        else:
            return 0.0

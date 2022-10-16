# InvalidParameterError.py
import Classes.errors.ClassesError as ClassesError

class InvalidParameterError(ClassesError.ClassesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg, function, parameter):
        super.__init__(self)
        self.msg = msg
        self.function = function
        self.parameter = parameter

    def __repr__(self) -> str:
        return f"{type(self).__name__} function={self.function}, parameter={self.parameter}, msg={self.msg}"

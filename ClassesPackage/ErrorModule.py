# ErrorModule.py
class Error(Exception):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str):
        self.msg = str(msg)

    def __repr__(self) -> str:
        return f"{type(self).__name__} (msg=\"{self.msg}\")"
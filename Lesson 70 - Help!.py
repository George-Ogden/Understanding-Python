from typing import Callable

class Helper:
    """Demonstrate docstrings

    Call help(Helper) to see this message.
    """
    def __init__(self):
        """Initialise Helper."""
    
    @staticmethod
    def function(x: int,func: Callable[[int],bool]) -> bool:
        """Return boolean value of func(x)."""
        return bool(func(x))

help(print)
help(list)
help(Helper)
help(Helper.__init__)
help(Helper.function)
print(Helper.function("hello", len))
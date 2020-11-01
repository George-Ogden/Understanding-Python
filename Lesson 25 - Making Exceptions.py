import logging

class OutOfBoundsError(ValueError):
    pass

level = int(input("What level should we log?\n"))
if level < 0:
    raise OutOfBoundsError("Level is too low")
elif level > 60:
    raise OutOfBoundsError("Level is too high")
logging.basicConfig(level=level)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
# exit(0)
quit(0)
logging.critical("Something has gone wrong")
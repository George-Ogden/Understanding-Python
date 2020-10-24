from .base import Base
print("imported file")
class File(Base):
    def __init__(self):
        super().__init__("folder/file")
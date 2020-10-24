from base import Base
print("imported subfile")
class File(Base):
    def __init__(self):
        super().__init__("subfolder/subfile")
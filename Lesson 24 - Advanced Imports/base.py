print("imported base")
class Base():
    def __init__(self,name="base"):
        self.name = name
        print("{} is initialised".format(self.name))
    def run(self):
        print("{} is running".format(self.name))
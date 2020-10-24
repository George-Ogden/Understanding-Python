print("imported alternative base")
class Base():
    def __init__(self,name="base"):
        self.name = name
        print("{} is initialised with an alternative base".format(self.name))
    def run(self):
        print("{} is running with an alternative base".format(self.name))
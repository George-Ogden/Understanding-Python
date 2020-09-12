class ExampleClass:
    def __init__(self,name):
        self.name = name
    def printName(self,value):
        print(self.name*value)
    def changeName(self,new_name):
        self.old_name = self.name
        self.name = new_name

instance1 = ExampleClass("instance1")
# instance2 = ExampleClass("instance2")
instance1.printName(2)
# instance2.printName(3)
instance1.changeName("instance")
instance1.printName(1)
print(instance1.old_name)
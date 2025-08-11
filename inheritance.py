
class shape:
    def __init__(self,name):
        self.name = name

    def describe(self):
        print(f"This shape is called {self.name}.")


class Rectangle(shape):
    def __init__(self,length,width):
        super().__init__("Rectangle")
        self.width=width
        self.length=length

    def area(self):
        a=self.width*self.length
        print(f"For {self.name} area is {a}.")
        return a

r1 = Rectangle(10,5)
r1.describe()
print(f"Length: {r1.length}, width: {r1.width}")
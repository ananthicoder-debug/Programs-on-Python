class GrandFather:
    def char(self):
        print("Tall")
class Father(GrandFather):
    def char(self):
        print("Tall and Intelligent")
class Child(Father):
    def char(self):
        print("Tall,Intelligent and Generous")
c1=Child()
print("Method Resolution Order:\n")
print(Child.mro())

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
[24bcs035@mepcolinux ex9]$python3 ex1.py
Method Resolution Order:

[<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.GrandFather'>, <class 'object'>]

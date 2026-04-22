class Father:
    def character(self):
        print("Genius")
class Mother:
    def character(self):
        print("Courageous")
class Child(Father,Mother):
    def character(self):
        print("Genius and Courageous\n")
c1=Child()
print("Child Character:")
c1.character()
print("Method Resolution Order:")
print(Child.mro())

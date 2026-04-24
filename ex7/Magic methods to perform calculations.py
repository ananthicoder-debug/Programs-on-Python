class Complex:
   def __init__(self,real,imag):
      self.real=real
      self.imag=imag
   def __add__(self,var):
      cno=complex((self.real+var.real),(self.imag+var.imag))
      return cno
   def __sub__(self,var):
      cno=complex((self.real-var.real),(self.imag-var.imag))
      return cno
   def display(self):
      print("Complex Number:",complex(self.real,self.imag))

print("Number1:")
c1=Complex(5,8)
c1.display()
print("Number2:")
c2=Complex(2,3)
c2.display()
print("Sum of 2 numbers:")
print(c1+c2)
print("Difference of two numbers:")
print(c1-c2)

class Book:
   def __init__(self,bname,bprice):
      self.bname=bname
      self.bprice=bprice
   def __add__(self,var):
      return (self.bprice+var.bprice)
   def display(self):
      print("Book name:",self.bname)
      print('Book Price:',self.bprice)

print("Book1 Details:")
b1=Book('Python',100)
b1.display()
print("Book2 Details:")
b2=Book('C++',300)
b2.display()
print("Total book price:" ,b1+b2)

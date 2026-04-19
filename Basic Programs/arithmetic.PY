print("1.Additon\n2.Subraction\n3.multiplication\n4.Division")
a,b=eval(input("Enter two numbers")).split(" ")
c=int(input("Enter your choice:"))
match c:
   case 1:
      print(a+b)
   case 2:
      print(a-b)
   case 3:
      print(a*b)
   case 4:
      print(a/b)

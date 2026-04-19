a,b,c=[int(i) for i in input("Enter 3 sides:").split(",")]
d=print("Valid Triangle") if (a+b)>c and (b+c)>a and (c+a)>b else print("Invalid Triangle:")

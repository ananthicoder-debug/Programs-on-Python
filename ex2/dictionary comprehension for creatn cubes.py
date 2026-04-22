ran=input("Enter the range for generating cubes:")
r1,r2=ran.split()
s={i:i**3 for i in range(int(r1),int(r2)+1)}
print(s)

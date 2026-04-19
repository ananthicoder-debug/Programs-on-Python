a,b,c=[int(i) for i in input("Enter 3 numbers:").split(",")]
d=sorted([a,b,c])
print("The second largest number:",d[-2])

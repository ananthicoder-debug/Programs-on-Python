import math
# Basic Mathematical Operations
num = float(input("Enter a number: "))

print(f"\nSquare root of {math.fabs(num)}: {math.sqrt(math.fabs(num))}")
print(f"Absolute value of {num}: {math.fabs(num)}")
print(f"Ceiling value of {num}: {math.ceil(num)}")
print(f"Floor value of {num}: {math.floor(num)}")
print(f"Power {num}^2: {math.pow((num), 2)}")
print(f"Exponential of {num}: {math.exp(num)}")
print("Round number:",round(num))

#Converting degree to radians
angle = float(input("\nEnter an angle in degrees: "))
radians = math.radians(angle)

print(f"{angle} in radians: {radians}")
print(f" Sin of {angle} : {math.sin(radians)}")
print(f"Cos od {angle} :{math.cos(radians)}")
# Constant
print(f"\nValue of pi: {math.pi}")

# GCD (Greatest Common Divisor)
a = int(input("\nEnter first integer for GCD: "))
b = int(input("Enter second integer for GCD: "))
print(f"GCD of {a} and {b}: {math.gcd(a, b)}")

#Logarithmic
print(f"Logarithmic value of 10: {math.log(10)}")

print("----Advanced mathematical Operations----")
n=5
r=2
permutation=math.factorial(n)/math.factorial(n-r)
print("Permutation of 5 anf 2:",int(permutation))

#Compound Interest
P=10000
r=0.05
t=5
A=P*math.pow((1+r),t)
print("Compound Interest:",A)

print("\nAll operations performed successfully!")

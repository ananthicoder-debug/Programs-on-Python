c=str(input("Enter a string:"))
if(c[::1]==c[::-1]):
   print("It is a palindrome")
else:
   print("It is not a palindrome")

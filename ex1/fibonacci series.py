n=int(input("Enter a number:"))
a,b,i=0,1,0
print("The fibbonacci series is ")
print(a,b,end=" ")
while i<n-2:
   c=a+b
   a=b
   b=c
   print(c,end=" ")
   i+=1
print()

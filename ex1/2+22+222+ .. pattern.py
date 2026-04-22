n=int(input("Enter a number:"))
sum,srow=0,0
for i in range(n):
   srow=(10*srow)+2
   sum+=srow
   print(srow,end="+")
print("\nThe sum of series is",sum)

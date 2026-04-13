c=int(input("Enter an amount:"))
note=[500,200,100]
rem=c
ncount={}
for i in note:
   if rem>=i:
      count=rem//i
      ncount[i]=count
      rem%=i
if not ncount and amount >0:
   print("This amount cannot be formed using 500,20,100")
else:
   for note,count in ncount.items():
      print(f"{note}:{count}")
   if rem>0:
      print("The remaining amount cannot be converted")

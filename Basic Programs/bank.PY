b=int(input("Enter the amount to withdraw:"))
c=int(input("Enter the acount balance:"))
a=print("balance:",c-b) if (c-b)>1500 and (b%100==0) else (print("Insufficient funds"))

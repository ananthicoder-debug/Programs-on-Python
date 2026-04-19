c=int(input("Enter the purchase amount:"))
d=print("Value after discount 20%",c-((c/100)*20)) if c>=5000 else (print("Value after discount for 10%",c-((c/100)*10)) if c>=3000 else print("No discount:",c))

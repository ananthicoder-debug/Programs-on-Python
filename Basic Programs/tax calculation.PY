c=int(input("Enter the basic salary:"))
d=print("Less than 2.5LPA No Tax",c) if c<=250000 else (print("2.5LPA-5LPA 5% tax",(c/100)*5) if 250000<c<=500000 else (print("5LPA-10LPA 10% tax",(c/100)*10) if 500000<c<=1000000 else print("Above 10LPA:",(c/100)*15)))

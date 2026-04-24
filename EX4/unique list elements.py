def distinct(l):
   l1=[]
   for i in l:
      if i not in l1:
         l1.append(i)
   return l1
num=list(eval(input("Enter list elements:")))
unique=distinct(num)
print("List with distinct elements is ",unique)

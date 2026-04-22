from zipfile import *
import os

f = ZipFile("f.zip", 'w', ZIP_DEFLATED)

for filename in ["f1.txt", "f2.txt", "f3.txt"]:
    if os.path.exists(filename):
        f.write(filename)
        print(f"{filename} added to zip.")
    else:
        print(f"{filename} not found.")

f.close()
print("\nf.zip file created successfully\n")

f = ZipFile("f.zip", 'r', ZIP_STORED)
n = f.namelist()

for n1 in n:
    print("File Name: ", n1)
    print("File data is:")
    f1 = open(n1, 'r')
    print(f1.read())
    print()

import os

print("\nFILE OPERATIONS MENU")
print("-------------------------")
print("1. Create a file")
print("2. Write to a file")
print("3. Read a file")
print("4. Append to a file")
print("5. Show file pointer using tell()")
print("6. Move file pointer using seek()")
print("7. Exit")

while True:

    print("-------------------------------")
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        filename = input("Enter filename to create: ")
        f = open(filename, 'w')
        f.close()
        print(filename, "created successfully.")

    elif choice == '2':
        filename = input("Enter filename to write to: ")
        if os.path.exists(filename):
            data = input("Enter data to write: ")
            f = open(filename, 'w')
            f.write(data)
            f.close()
            print("Data written successfully.")
        else:
            print("File does not exist.")

    elif choice == '3':
        filename = input("Enter filename to read: ")
        if os.path.exists(filename):
            f = open(filename, 'r')
            print("File contents:\n", f.read())
            f.close()
        else:
            print("File does not exist.")

    elif choice == '4':
        filename = input("Enter filename to append to: ")
        if os.path.exists(filename):
            data = input("Enter data to append: ")
            f = open(filename, 'a')
            f.write(data)
            print("Data appended successfully.")
            f.close()
        else:
            print("File does not exist.")

    elif choice == '5':
        filename = input("Enter filename to show file pointer position: ")
        f=open(filename,'r')
        if os.path.exists(filename):
            f.read(3)
            print("File pointer position after reading three characters is:", f.tell())
            f.close()
        else:
            print("File does not exist.")

    elif choice == '6':
        filename = input("Enter filename to seek into: ")
        if os.path.exists(filename):
            pos = int(input("Enter position to move file pointer to: "))
            f = open(filename, 'r')
            f.seek(pos)
            print("Pointer moved. Current position:", f.tell())
            print("Data from that position:\n", f.read())
            f.close()
        else:
            print("File does not exist.")

    elif choice == '7':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")

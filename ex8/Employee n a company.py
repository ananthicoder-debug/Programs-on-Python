import gc

class Employee:

    class Address:
        def __init__(self, street, city, state, pincode):
            self.street = street
            self.city = city
            self.state = state
            self.pincode = pincode

        def display_address(self):
            print(f"Address: {self.street}, {self.city}, {self.state} - {self.pincode}")

    def __init__(self, emp_id, name, street, city, state, pincode):
        self.emp_id = emp_id
        self.name = name
        self.address = Employee.Address(street, city, state, pincode)
        print(f"Employee {self.name} (ID: {self.emp_id}) is hired.")

    def display_info(self):
        print(f"\nEmployee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        self.address.display_address()

    def __del__(self):
        print(f"Employee {self.name} (ID: {self.emp_id}) has resigned.")

emp1 = Employee(101, "Vish", "12 Park Street", "Chennai", "Tamil Nadu", 600001)
emp2 = Employee(102, "Shal", "45 Lake View", "Bengaluru", "Karnataka", 560001)

emp1.display_info()
emp2.display_info()

del emp1
gc.collect()

print("\nAfter some time...")

del emp2
gc.collect()

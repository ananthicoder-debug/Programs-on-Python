class Supplier:
    all_suppliers = []

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        Supplier.all_suppliers.append(self)

    def display_info(self):
        print(f"Supplier Name: {self.name}")
        print(f"Contact Info: {self.contact}")

    @classmethod
    def get_supplier_count(cls):
        return len(cls.all_suppliers)


class Product:
    all_products = []

    class Specification:
        def __init__(self, color):
            self.color = color

        def display_spec(self):
            print(f"Color: {self.color}")

    def __init__(self, name, price, supplier, color):
        self.name = name
        self.price = price
        self.supplier = supplier
        self.spec = Product.Specification(color)
        Product.all_products.append(self)

    def display_info(self):
        print(f"\nProduct Name: {self.name}")
        print(f"Price: Rs.{self.price}")
        print("Supplier Information:")
        self.supplier.display_info()
        print("Product Specification:")
        self.spec.display_spec()

    @classmethod
    def get_product_count(cls):
        return len(cls.all_products)

supplier1 = Supplier("Fresh Farms", "freshfarms@example.com")
supplier2 = Supplier("Green Growers", "greengrowers@example.com")

product1 = Product("Organic Apple", 150, supplier1, "Red")
product2 = Product("Organic Banana", 60, supplier2, "Yellow")
product3 = Product("Organic Carrot", 80, supplier1, "Orange")

product1.display_info()
product2.display_info()
product3.display_info()

print("\nTotal Products:", Product.get_product_count())
print("Total Suppliers:", Supplier.get_supplier_count())

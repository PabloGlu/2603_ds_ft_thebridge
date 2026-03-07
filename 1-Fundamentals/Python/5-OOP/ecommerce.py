# ecommerce.py
class Product:
    """
    Represents a product with a SKU, name, and price.
    """

    def __init__(
        self,
        sku: str,
        name: str,
        price: float,
    ):
        """
        Initializes a new Product instance.

        Args:
            sku (str): The Stock Keeping Unit, a unique identifier for the product.
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.sku = sku
        self.name = name
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string showing the product's name, SKU, and price.
        """
        str_producto = (f"{str(self.name)}:  \n sku: {str(self.sku)} \n price: {str(self.price)}")
        print(str_producto)
        return str_producto

class Shoes(Product):
    """
    Represents a shoe product, inheriting from Product, with additional attributes for size and color.
    """

    def __init__(
        self,
        sku: str,
        name: str,
        price: float,
        size: int,
        color: str,
    ):
        """
        Initializes a new Shoes instance.

        Args:
            sku (str): The Stock Keeping Unit.
            name (str): The name of the shoe.
            price (float): The price of the shoe.
            size (int): The size of the shoe.
            color (str): The color of the shoe.
        """
        super().__init__(sku, name, price)
        self.size = size
        self.color = color

    def __str__(self):
        """
        Returns a string representation of the shoe, including details from the parent Product class.

        Returns:
            str: A string showing shoe details, including size and color.
        """
        str_producto = (f"{str(self.name)}:  \n sku: {str(self.sku)} \n price: {str(self.price)}")
        str_shoes = str_producto + (f"\n size: {str(self.size)} \n color: {str(self.color)}")
        
        print(str_shoes)
        return str_shoes

class Electronics(Product):
    """
    Represents an electronics product, inheriting from Product, with additional attributes for brand and warranty.
    """

    def __init__(
        self,
        sku: str,
        name: str,
        price: float,
        brand: str,
        warranty_period: int,
    ):
        """
        Initializes a new Electronics instance.

        Args:
            sku (str): The Stock Keeping Unit.
            name (str): The name of the electronic device.
            price (float): The price of the device.
            brand (str): The brand of the device.
            warranty_period (int): The warranty period in months.
        """
        super().__init__(sku, name, price)
        self.brand = brand
        self.warranty_period = warranty_period

    def __str__(self):
        """
        Returns a string representation of the electronics product, including details from the parent Product class.

        Returns:
            str: A string showing electronics details, including brand and warranty.
        """
        str_producto = (f"{str(self.name)}:  \n sku: {str(self.sku)} \n price: {str(self.price)}")
        str_electro = str_producto + (f"\n brand: {str(self.brand)} \n warranty: {str(self.warranty_period)}")
        
        print(str_electro)
        return str_electro
    
class Furniture(Product):
    """
    Represents a furniture product, inheriting from Product, with attributes for material and dimensions.
    """

    def __init__(
        self,
        sku: str,
        name: str,
        price: float,
        material: str,
        dimensions: str,
    ):
        """
        Initializes a new Furniture instance.

        Args:
            sku (str): The Stock Keeping Unit.
            name (str): The name of the furniture item.
            price (float): The price of the item.
            material (str): The material the furniture is made of.
            dimensions (str): The dimensions of the furniture (e.g., "36x24x18 inches").
        """
        super().__init__(sku, name, price)
        self.material = material
        self.dimensions = dimensions
    def __str__(self):
        """
        Returns a string representation of the furniture product, including details from the parent Product class.

        Returns:
            str: A string showing furniture details, including material and dimensions.
        """
        str_producto = (f"{str(self.name)}:  \n sku: {str(self.sku)} \n price: {str(self.price)}")
        str_furniture = str_producto + (f"\n material: {str(self.material)} \n dimensions: {str(self.dimensions)}")
        
        print(str_furniture)
        return str_furniture

class Warehouse:
    """
    Manages the inventory of products.
    """

    def __init__(
        self,
        company_name: str,
    ):
        """
        Initializes a new Warehouse instance.

        Args:
            company_name (str): The name of the company that owns the warehouse.
        """
        self.company_name = company_name
        self.storage = []

    def __str__(self) -> str:
        """
        Returns a string representation of the warehouse.

        Returns:
            str: A string indicating the warehouse's company name.
        """
        print(self.company_name)
        return self.company_name

    def add_product(
        self,
        product: Product,
    ) -> None:
        """
        Adds a single product instance to the warehouse inventory.

        Args:
            product (Product): The product to add.

        Returns:
            None
        """
        self.storage.append(product)
        
        return None
    

    def remove_product(
        self,
        product: Product,
    ) -> Product | None:
        """
        Removes a single, specific product instance from the warehouse inventory.

        Args:
            product (Product): The product instance to remove.  This must be the *exact*
                               object in the inventory, not just one with the same SKU.

        Returns:
            Product | None: The removed product instance if found and removed, otherwise None.
                            Prints an error message if the product is not found.
        """
        if product in self.storage:
            self.storage.remove(product)
            print('Product removed: ')
            return product.__str__()
        else:
            raise Exception('Product not found')
    count = 0
    def count_product(self, prod):
        count = 0
        for product in self.storage:
            if prod == product:
                count += 1
        # print(prod.name, count)
        return prod.name, count
    

    def count_all(self):
        counter = 0
        seen = []
        for product in self.storage:
            self.count_product(product)
            seen.append(self.count_product(product))
        print(f"Total Storage: {dict(seen)}")

            
        

    def calculate_total_value(self) -> float:
        """
        Calculates the total value of all products currently in the warehouse.

        Returns:
            float: The total value (sum of all product prices).
        """
        
        total_value = 0
        for product in self.storage:
            total_value += product.price
        print('Actual total value in storage:')
        print(total_value)
        return total_value

    def get_current_inventory(self) -> None:
        """
        Prints the current inventory of the warehouse.  Displays each product's name,
        SKU, quantity, and the total value of the warehouse.

        Returns:
            None
        """
        products = []
        print('Storage -->')
        for product in self.storage:
            products.append((product.name, product.sku))
        print(dict(products))
        self.count_all()
        print(f"Total value from current inventory: {self.calculate_total_value()}")
        return None

    def add_multiple_products(
        self,
        product: Product,
        quantity: int,
    ) -> None:
        """
        Adds multiple copies of the *same* product instance to the warehouse.

        Args:
            product (Product): The product instance to add.  All added products will
                               be this exact object (important for later removal).
            quantity (int): The number of copies to add.

        Returns:
            None. Prints an error message if the quantity is not positive.
        """
        try:
            if quantity < 0:
                for i in range(quantity):
                    self.storage.append(product)
            else:
                print('Quantity must be positive')
        except:
            None

    def remove_multiple_products(
        self,
        sku: str, # Puedes indicar sku o nombre, a tu eleccion
        quantity: int,
    ) -> int:
        """
        Removes multiple products with the given SKU from the warehouse.

        Args:
            sku (str): The SKU of the products to remove.
            quantity (int): The number of products to attempt to remove.

        Returns:
            int: The number of products actually removed.  This may be less than
                 `quantity` if there aren't enough products with the given SKU
                 in the warehouse. Prints error messages if the SKU is not found
                 or if the quantity is invalid.
        """
        try:
            if sku in self.storage:
                count = 0 
                for i in range(quantity):
                    self.storage.remove(sku) 
                    count += 1
                    if sku not in self.storage:
                        print(f"There was only {count} {sku.name}\n No more {sku.name} in storage")
                        return count


                print(f"Removed {count} {sku.name}, {self.count_product(sku)[1]} {self.count_product(sku)[0]} left")
                return count
                
        except Exception as e:
            print('All removed')
            print(e)

        



p1 = Product(116523, 'Objeto', 25)
p1.__str__()

s1 = Shoes(123342, 'Zapato', 35, 47, 'lila')
s1.__str__()

e1 = Electronics(123142, 'Electrodomestico', 101, 'lg', 3)
e1.__str__()

f1 = Furniture(324323, 'Mueble', 234, 'madera', '135 x 250')
f1.__str__()

warehouse_1 = Warehouse('Taiga')

warehouse_1.add_product(p1)
warehouse_1.add_product(s1)
warehouse_1.add_product(e1)
warehouse_1.get_current_inventory()
warehouse_1.remove_product(e1)
warehouse_1.get_current_inventory()
warehouse_1.calculate_total_value()
warehouse_1.add_product(e1)
warehouse_1.get_current_inventory()
warehouse_1.calculate_total_value()
warehouse_1.add_multiple_products(f1, 3)
warehouse_1.get_current_inventory()
warehouse_1.count_product(f1)
warehouse_1.count_all()
warehouse_1.remove_multiple_products(f1, 2)
warehouse_1.count_all()
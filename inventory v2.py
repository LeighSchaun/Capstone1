
# Creating a class named shoes
class Shoes:

     """
    A class representing a shoe item.

    Attributes:
        country (str): The country of origin of the shoe.
        code (str): The code of the shoe.
        product (str): The name of the shoe product.
        cost (float): The cost of the shoe.
        quantity (int): The quantity of the shoe.
    """

    # Attributes for the shoe class
    def __init__(self, country, code, product, cost, quantity):

        """
        Initializes a new instance of the Shoes class.

        Args:
            country (str): The country of origin of the shoe.
            code (str): The code of the shoe.
            product (str): The name of the shoe product.
            cost (float): The cost of the shoe.
            quantity (int): The quantity of the shoe.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    # Defining the get cost method to return the cost of the shoes
    def get_cost(self):

        """
        Returns the cost of the shoe.
        """
        return self.cost

    # Defining the get quantity method to return the quantity of the shoes
    def get_quantity(self):

        """
        Returns the quantity of the shoe.
        """
        return self.quantity
    # Defining __str__ method to return the string representation of a class shoes
    def __str__(self):

        """
        Returns the string representation of a Shoes object.
        """
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# Creating a list t store all shoes
shoes_list = []

# Defing the get shoes method to read the details from the inventory.txt file
# Opens the text file to read content
# Converst cost to float
# Converts quantity to an integer
def read_shoes_data():
    with open("inventory.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i == 0:
                continue  # skip first line
            country, code, product, cost, quantity = line.strip().split(",")
            cost = float(cost)  
            quantity = int(quantity)  
            shoe = Shoes(country, code, product, cost, quantity)
            shoes_list.append(shoe)
            
# Defining the capture shoes function that request the user to capture details requred for the shoe
# Appends the new shoe to the Shoes_list
def capture_shoes():


    """
    Captures details required for a new shoe item and adds it to the Shoes list.
    """
    country = input("Enter the country of origin: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the product name: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe = Shoes(country, code, product, cost, quantity)
    shoes_list.append(shoe)

# Defins the function for user to view all shoes
def view_all():

    """
    Prints all the Shoe objects in the Shoes list.
    """

    print("All shoes:")
    print()
    for shoe in shoes_list:
        print(shoe)
        
# Defining a function that finds the shoe object with the lowest quantity taht needs to be re-stocked
# Asks the user if the user wants to add more of these shoes
# Updates the quantity on this shoe
def re_stock():

    """
    Finds the Shoe object with the lowest quantity that needs to be re-stocked,
    asks the user if they want to add more of these shoes, and updates the quantity on this shoe.
    """

    lowest_quantity_shoe = min(shoes_list, key=lambda x: x.quantity)
    add_quantity = int(input(f"Do you want to add more {lowest_quantity_shoe.product} shoes? Enter quantity: "))
    lowest_quantity_shoe.quantity += add_quantity

# Defining a funton to search for shoes by shoe code
# If the shoe code is found, the shoe for that code is returned, if not found the function returns none
def search_shoe(code):

    """
    Searches for a Shoe object in the Shoes list based on a given shoe code.

    Args:
        code (str): The code of the shoe to search for.

    Returns:
        (Shoes object): The Shoe object with the given code, if found. None otherwise.
    """

    for shoe in shoes_list:
        if shoe.code == code:
            return shoe
    return None

# Defining a function to canculate the total value for each item
def value_per_item():
    """
Calculates and prints the total value for each shoe in the shoes list.
The total value is calculated by multiplying the cost of each shoe with its quantity.
"""
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}:  R{value}")
        
# Defining a function to find the shoe with the highest quantity
# Prints to the user this shoe is for sale
def highest_qty():

    """
Finds the shoe with the highest quantity in the shoes list and prints a message
to the user indicating that this shoe is for sale.
"""
    highest_quantity_shoe = max(shoes_list, key=lambda x: x.quantity)
    print(f"{highest_quantity_shoe.product} is for sale")

# Calls the read shoes data function
read_shoes_data()

# Menu is dsplayed as long as the user did not select exit
while True:
    print("1. Capture shoe data")
    print("2. View all shoes")
    print("3. Re-stock shoes")
    print("4. Search for a shoe")
    print("5. Calculate value per item")
    print("6. Determine highest quantity shoe for sale")
    print("7. Exit")

    # Request the user to make a selection
    choice = int(input("Enter your choice by selecting the number of the option: "))

    # Checks which option the user selected and calls the appropriate function
    if choice == 1:
        capture_shoes()
    elif choice == 2:
        view_all()
    elif choice == 3:
        re_stock()
    elif choice == 4:
        code = input("Enter the shoe code: ")
        shoe = search_shoe(code)
        if shoe:
            print(shoe)
        else:
            print("Shoe not found")
    elif choice == 5:
        value_per_item()
    elif choice == 6:
        highest_qty()
    elif choice == 7:
        exit()

        break
    # Prints if the user made an invalid selection
    else:
        print("Invalid choice")



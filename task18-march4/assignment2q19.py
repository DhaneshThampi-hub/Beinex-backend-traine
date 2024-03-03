"""19.Write program for building restaurant menu using class in Python."""


# Define a class representing a menu item
class MenuItem:
    def __init__(self, name, description, price):
        # Initialize a menu item with a name, description, and price
        self.name = name
        self.description = description
        self.price = price


# Define a class representing a restaurant menu
class RestaurantMenu:
    def __init__(self):
        # Initialize a restaurant menu with an empty list of menu items
        self.menu_items = []

    def add_menu_item(self, menu_item):
        # Method to add a menu item to the restaurant menu
        self.menu_items.append(menu_item)

    def display_menu(self):
        # Method to display the restaurant menu
        if not self.menu_items:
            print("No items in the menu.")
        else:
            print("Restaurant Menu:")
            for item in self.menu_items:
                print(f"{item.name} - {item.description} - ${item.price:.2f}")


# Function to get user input for adding a menu item
def get_menu_item_input():
    # Prompt the user for input to create a new menu item
    name = input("Enter the name of the dish: ")
    description = input("Enter the description of the dish: ")
    price = float(input("Enter the price of the dish: $"))
    return MenuItem(name, description, price)


# Example usage with user-friendly features:
menu = RestaurantMenu()

while True:
    print("\nChoose an option:")
    print("1 - Add a Menu Item")
    print("2 - Display Menu")
    print("3 - Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        # User chooses to add a menu item
        menu_item = get_menu_item_input()
        menu.add_menu_item(menu_item)
        print(f"{menu_item.name} added to the menu.")
    elif choice == "2":
        # User chooses to display the menu
        menu.display_menu()
    elif choice == "3":
        # User chooses to exit the program
        print("Exiting the program.")
        break
    else:
        # Handle invalid choices
        print("Invalid choice. Please enter a number between 1 and 3.")



# Crusty's Pizza Ordering System V3
# This program allows customers to order pizzas from Crusty's Pizza.
# It supports both pickup and delivery orders, and provides a menu for regular and gourmet pizzas.
# The program also includes features for canceling and modifying orders, as well as a kitchen screen
# to display all orders.

# Function to get a valid name from the user
def get_valid_name():
    """
    Prompts the user to enter a customer's name and validates that it contains only alphabetic characters
    Returns the valid name.
    """
    while True:
        name = input("Please enter the customer's name: ")
        if name.isalpha():
            return name
        else:
            print("Invalid name. Please try again.")

# Function to get a valid phone number from the user
def get_valid_phone_number():
    """
    Prompts the user to enter a customer's phone number and validates that it contains only digits
    and has a maximum length of 10 characters.
    Returns the valid phone number.
    """
    while True:
        phone_number = input("Please enter the customer's phone number: ")
        if phone_number.isdigit() and len(phone_number) <= 10:
            return phone_number
        else:
            print("Invalid phone number. Please enter up to 10 digits only.")

# Function to display the pizza menu
def display_pizza_menu(regular_pizzas, gourmet_pizzas):
    """
    Displays the pizza menu with the pizza names and prices.
    Takes two lists as parameters: regular_pizzas and gourmet_pizzas.
    """
    print("\nCRUSTY'S PIZZA MENU")
    print("Regular Pizzas: $8.50")
    for i, pizza in enumerate(regular_pizzas, start=1):
        print(f"{i}. {pizza}")
    print("\nGourmet Pizzas: $13.50")
    for i, pizza in enumerate(gourmet_pizzas, start=8):
        print(f"{i}. {pizza}")

# Function to get pizza orders from the user
def get_pizza_orders(num_pizzas, regular_pizzas, gourmet_pizzas):
    """
    Prompts the user to enter their pizza choices and returns a list of ordered pizzas and the total cost.
    Takes the number of pizzas to order and the two pizza lists as parameters.
    """
    pizzas_ordered = []
    total_cost = 0.0
    for _ in range(num_pizzas):
        pizza_choice = int(input(f"Please enter the number of the pizza you would like to order (1-7 for regular, 8-12 for gourmet): "))
        if 1 <= pizza_choice <= 7:
            pizzas_ordered.append(["Regular", regular_pizzas[pizza_choice - 1]])
            total_cost += 8.50
        elif 8 <= pizza_choice <= 12:
            pizzas_ordered.append(["Gourmet", gourmet_pizzas[pizza_choice - 8]])
            total_cost += 13.50
        else:
            print("Invalid pizza choice. Please try again.")
            continue  # Skip to the next iteration of the loop
    return pizzas_ordered, total_cost

# Welcome message
print("Welcome to Crusty's Pizza!")

# List to store all orders
all_orders = []

# Loop until the user chooses to exit
while True:
    # Get order type (pickup or delivery)
    order_type = input("Is this order for pickup or delivery? (Enter 'pickup' or 'delivery'): ").lower()

    # Initialise order details
    customer_name = ""
    customer_address = ""
    customer_phone = ""
    delivery_charge = 0.0
    pizzas_ordered = []
    total_cost = 0.0

    # Gets customer details based on order type
    if order_type == "delivery":
        customer_name = get_valid_name()
        customer_address = input("Please enter the customer's address: ")
        customer_phone = get_valid_phone_number()
        delivery_charge = 2.50  # Delivery charge for delivery orders
    elif order_type == "pickup":
        customer_name = get_valid_name()
    else:
        print("Invalid order type. Please try again.")
        continue  # Skip to the next iteration of the loop

    # Define the pizza lists
    regular_pizzas = ["Pepperoni", "Hawaiian", "Cheese", "Meat Lovers", "BBQ Beef & Onion", "Italian", "Mushroom"]
    gourmet_pizzas = ["Zesty Zucchini", "Salty Sardine", "Meaty Maven", "Vegetarian Viva", "Jalapeño Jolt"]

    # Display the pizza menu
    display_pizza_menu(regular_pizzas, gourmet_pizzas)

    # Get the pizza orders
    num_pizzas = int(input("\nHow many pizzas would you like to order? (Maximum 5): "))
    if num_pizzas > 5:
        print("Sorry, the maximum number of pizzas per order is 5.")
        continue  # Skip to the next iteration of the loop

    pizzas_ordered, total_cost = get_pizza_orders(num_pizzas, regular_pizzas, gourmet_pizzas)

    # Display the order summary
    print("\nOrder Summary:")
    for pizza in pizzas_ordered:
        print(f"- {pizza[0]} Pizza: {pizza[1]}")
    print(f"Total Cost: ${total_cost + delivery_charge:.2f}")
    if order_type == "delivery":
        print(f"Delivery Charge: ${delivery_charge:.2f}")
    print(f"Customer Name: {customer_name}")

    # Management summary
    total_pizzas_sold = len(pizzas_ordered)
    total_revenue = total_cost + delivery_charge
    print("\nManagement Summary:")
    print(f"Total Pizzas Sold: {total_pizzas_sold}")
    print(f"Total Revenue: ${total_revenue:.2f}")

    # Store the current order in the all_orders list
    current_order = {
        "customer_name": customer_name,
        "order_type": order_type,
        "pizzas_ordered": pizzas_ordered,
        "total_cost": total_cost,
        "delivery_charge": delivery_charge,
        "customer_phone": customer_phone
    }
    all_orders.append(current_order)

    # Kitchen screen
    print("\nKitchen Screen:")
    for i, order in enumerate(all_orders, start=1):
        print(f"Order {i}:")
        for j, pizza in enumerate(order["pizzas_ordered"], start=1):
            print(f"{j}. {pizza[0]} Pizza: {pizza[1]}")
        print(f"Customer Name: {order['customer_name']}")
        print(f"Order Type: {order['order_type']}")
        print(f"Total Cost: ${order['total_cost'] + order['delivery_charge']:.2f}")
        if order["order_type"] == "delivery":
            print(f"Delivery Charge: ${order['delivery_charge']:.2f}")
        print(f"Customer Phone: {order['customer_phone']}")
        print()

    # Cancel order
    cancel_order = input("\nWould you like to cancel the order? (Enter 'yes' or 'no'): ").lower()
    while cancel_order not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        cancel_order = input("Would you like to cancel the order? (Enter 'yes' or 'no'): ").lower()

    if cancel_order == "yes":
        print("Order has been cancelled.")
        all_orders.pop()  # Remove the last order from the all_orders list
    else:
        print("Thank you for your order!")

    # Modify order
    modify_order = input("\nWould you like to modify an order? (Enter 'yes' or 'no'): ").lower()
    while modify_order not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        modify_order = input("Would you like to modify an order? (Enter 'yes' or 'no'): ").lower()

    if modify_order == "yes":
        order_number = int(input("Enter the order number you want to modify: "))
        if order_number > 0 and order_number <= len(all_orders):
            order_to_modify = all_orders[order_number - 1]
            print(f"\nCurrent Order Details:")
            print(f"Customer Name: {order_to_modify['customer_name']}")
            print(f"Order Type: {order_to_modify['order_type']}")
            for i, pizza in enumerate(order_to_modify["pizzas_ordered"], start=1):
                print(f"{i}. {pizza[0]} Pizza: {pizza[1]}")
            print(f"Total Cost: ${order_to_modify['total_cost'] + order_to_modify['delivery_charge']:.2f}")
            if order_to_modify["order_type"] == "delivery":
                print(f"Delivery Charge: ${order_to_modify['delivery_charge']:.2f}")
            print(f"Customer Phone: {order_to_modify['customer_phone']}")

            modify_choice = input("\nWhat would you like to modify? (Enter 'name', 'address', 'phone', 'pizzas', or 'cancel'): ").lower()
            if modify_choice == "name":
                while True:
                    new_name = input("Enter the new customer name: ")
                    if new_name.isalpha():
                        order_to_modify["customer_name"] = new_name
                        break
                    else:
                        print("Invalid name. Please try again.")
            elif modify_choice == "address":
                new_address = input("Enter the new customer address: ")
                order_to_modify["customer_address"] = new_address
            elif modify_choice == "phone":
                new_phone = input("Enter the new customer phone number: ")
                order_to_modify["customer_phone"] = new_phone
            elif modify_choice == "pizzas":
                new_pizzas = []
                num_new_pizzas = int(input("How many pizzas would you like to order? (Maximum 5): "))
                if num_new_pizzas > 5:
                    print("Sorry, the maximum number of pizzas per order is 5.")
                else:
                    for _ in range(num_new_pizzas):
                        pizza_choice = int(input(f"Please enter the number of the pizza you would like to order (1-7 for regular, 8-12 for gourmet): "))
                        if 1 <= pizza_choice <= 7:
                            new_pizzas.append(["Regular", regular_pizzas[pizza_choice - 1]])
                        elif 8 <= pizza_choice <= 12:
                            new_pizzas.append(["Gourmet", gourmet_pizzas[pizza_choice - 8]])
                        else:
                            print("Invalid pizza choice. Please try again.")
                            break
                    order_to_modify["pizzas_ordered"] = new_pizzas
                    order_to_modify["total_cost"] = sum(13.50 if pizza[0] == "Gourmet" else 8.50 for pizza in new_pizzas)
            elif modify_choice == "cancel":
                print("Modification cancelled.")
            else:
                print("Invalid choice. Modification cancelled.")
        else:
            print("Invalid order number.")

    # Ask if the user wants to place another order or exit
    another_order = input("\nWould you like to place another order? (Enter 'yes' or 'no'): ").lower()
    while another_order not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        another_order = input("Would you like to place another order? (Enter 'yes' or 'no'): ").lower()

    if another_order == "no":
        print("Thank you for using Crusty's Pizza Ordering System. Goodbye!")
        break  # Exit the loop
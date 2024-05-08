# Crusty's Pizza Ordering System V1

# Welcome message
print("Welcome to Crusty's Pizza!")

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
    customer_name = input("Please enter the customer's name: ")
    customer_address = input("Please enter the customer's address: ")
    customer_phone = input("Please enter the customer's phone number: ")
    delivery_charge = 2.50
elif order_type == "pickup":
    customer_name = input("Please enter the customer's name: ")
else:
    print("Invalid order type. Please try again.")
    exit()

# Define the pizza lists
regular_pizzas = ["Pepperoni", "Hawaiian", "Cheese", "Meat Lovers", "BBQ Beef & Onion", "Italian", "Mushroom"]
gourmet_pizzas = ["Zesty Zucchini", "Salty Sardine", "Meaty Maven", "Vegetarian Viva", "Jalapeño Jolt"]

# Display the pizza menu
print("\nCRUSTY'S PIZZA MENU")
print("Regular Pizzas: $8.50")
for i, pizza in enumerate(regular_pizzas):
    print(f"{i+1}. {pizza}")
print("\nGourmet Pizzas: $13.50")
for i, pizza in enumerate(gourmet_pizzas):
    print(f"{i+1}. {pizza}")

# Get the pizza orders
num_pizzas = int(input("\nHow many pizzas would you like to order? (Maximum 5): "))
if num_pizzas > 5:
    print("Sorry, the maximum number of pizzas per order is 5.")
    exit()

for i in range(num_pizzas):
    pizza_choice = int(input(f"Please enter the number of the pizza you would like to order (1-7 for regular, 8-12 for gourmet): "))
    if pizza_choice >= 1 and pizza_choice <= 7:
        pizzas_ordered.append(["Regular", regular_pizzas[pizza_choice - 1]])
        total_cost += 8.50
    elif pizza_choice >= 8 and pizza_choice <= 12:
        pizzas_ordered.append(["Gourmet", gourmet_pizzas[pizza_choice - 8]])
        total_cost += 13.50
    else:
        print("Invalid pizza choice. Please try again.")
        exit()

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

# Kitchen screen
print("\nKitchen Screen:")
for i, pizza in enumerate(pizzas_ordered):
    print(f"{i+1}. {pizza[0]} Pizza: {pizza[1]}")

# Cancel order
cancel_order = input("\nWould you like to cancel the order? (Enter 'yes' or 'no'): ").lower()
if cancel_order == "yes":
    print("Order has been cancelled.")
else:
    print("Thank you for your order!")
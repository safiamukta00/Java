import random

menu = {
    'Burger': 50,
    'Coffee': 40,
    'Salad': 70,
    'Pasta': 60,
    'Pizza': 190,
    'Tea': 20,
    'Sandwich': 65,
    'Roll': 30,
    'Cake': 80,
}

inventory = {
    'Burger': 10,
    'Coffee': 10,
    'Salad': 10,
    'Pasta': 10,
    'Pizza': 10,
    'Tea': 10,
    'Sandwich': 10,
    'Roll': 10,
    'Cake': 10,
}

print('Welcome to Cafe Sunrise')
print('Menu:')
for item, price in menu.items():
    print(f"{item}: Tk-{price}")

total_order = 0
ordered_items = []

def predict_demand(item):
    demand_factor = random.uniform(0.9, 1.1)
    predicted_demand = int(inventory[item] * demand_factor)
    print(f"Predicted demand for {item} tomorrow: {predicted_demand} items")

while True:
    items_input = input("Enter the names of items you want to order (separate with commas): ")
    items = [item.strip() for item in items_input.split(',')]

    for item in items:
        if item in menu:
            if inventory[item] > 0:
                total_order += menu[item]
                ordered_items.append(item)
                inventory[item] -= 1
                print(f'Your item {item} has been added to your order')
            else:
                print(f'Sorry, {item} is out of stock.')
        else:
            print(f'Ordered item {item} is not available yet!')

    another_order = input("Do you want to order another item? (Yes/No): ").strip().lower()
    if another_order != "yes":
        break

ordered_items_list = ", ".join(ordered_items)
print(f"\nYour order: {ordered_items_list}")
print(f'The total amount of your order is: Tk-{total_order}')

print("\nDemand prediction for the next day:")
for item in inventory:
    predict_demand(item)
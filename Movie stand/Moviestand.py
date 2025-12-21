# Generate a pyton program to for movie stand that hold some food items

menu = {"pizza": 3, "popcorn": 5, "fries": 4}
cart = []
total = 0

print("-------- MENU --------")

for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("----------------------")

while True:
    food = input("Enter the food you want to order (q to quit): ").lower()

    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        total += menu.get(food)
        print(f"{food} added to cart.")
    else:
        print("Item is not available")

print("\nYour cart contains:")
for item in cart:
    print("-", item)

print(f"\nYour total amount is: ${total:.2f}")
print("Enjoy your movie 🎬🍿")


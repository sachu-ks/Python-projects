# Shopping cart program

# we are  creating a simple shopping cart program to accept the list of foods and amount from the customer.
# output should be total shopping cart and total amount

foods=[]
prices=[]
Total= 0

while True:
    food=input("Enter the food item that you need to buy (q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the amount of {food}:$ "))
        foods.append(food)
        prices.append(price)

print(">>>>Your Cart<<<<")

for food in foods:
    print(food, end=" ")

print()

for price in prices:
    Total = Total + price

print(f"Your total amount is {Total}$")

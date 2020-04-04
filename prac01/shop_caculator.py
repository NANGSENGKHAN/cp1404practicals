# If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the
# screen.

number_of_items = int(input("Enter number of items: "))

list1 = []
for i in range(1, number_of_items + 1, 1):
    price = float(input("Price of item: "))
    list1.append(price)

total_price = sum(list1)

if total_price > 100:
    final_price = total_price * 0.9
else:
    final_price = total_price
print("Total price for {} items is ${:2f}".format(number_of_items, final_price))
import random

maximum_increase = 0.175  # 17.5%
maximum_decrease = 0.05  # 5%
initial_price = 10.0
minimum_price = 0.01  # 1%
maximum_price = 1000
OUTPUT_FILE = "stock_output.txt"

# open output file for writing (this creates a new file if it doesn't exist)
out_file = open(OUTPUT_FILE, 'w')

price = initial_price
day = 0
print("Starting price: ${:,.2f}".format(price), file=out_file)

while price >= minimum_price and price <= maximum_price:
    price_change = 0
    day = 1 + day
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, maximum_price)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-maximum_decrease, 0)

    price *= (1 + price_change)
    # print("On day {} price is: ${:,.2f}".format(day, price))
    print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)

# don't forget to close the file when we've finished with it
out_file.close()

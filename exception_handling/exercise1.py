prices = []
while True:
    price_input = input("Enter Original Prices (or) Type 'done' to finish : ")
    if price_input.lower() == 'done':
        break
    try:
        price = float(price_input)
        prices.append(price)
    except ValueError:
        print("Enter a valid price (or) 'done' to stop")

if prices:
    print("\nOriginal Prices Are : ")
    for x in prices:
        print(f"{x} Ks")
    print(f"Enumerated Original Prices : {list(enumerate(prices))} \n")

    while True:
        try:
            discount_input = float(input("Enter Discount in % : "))

            if 0 < discount_input < 100:
                discount_percentage = (100 - discount_input) / 100

                for i, discount in enumerate(prices):
                    prices[i] = discount * discount_percentage

                print(f"Promotion Prices are : ")
                for x in prices:
                    print(f"{round(x, 2)} Ks")
                break
            else:
                print("Discount % Must Be Between 0 And 100!")
        except ValueError:
            print("Invalid Discount Input! Enter a number")

else:
    print("\n No Prices were entered!")
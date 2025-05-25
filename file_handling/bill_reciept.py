from fpdf import FPDF

customer_name = input("Enter customer name : ").title().strip()
products = []

while True:
    product_name = input("\nEnter product name (or) press Enter to finish : ")
    if product_name == '':
        break

    while True:
        price = input("Price : ")
        try:
            price = float(price)
            break
        except ValueError:
            print("Price must be integer or float!")

    while True:
        qty = input("Quantity : ")
        try:
            qty = int(qty)
            break
        except ValueError:
            print("Quantity must be integer!")

    total = qty * price
    products.append((product_name,price,qty,total))

sub_total = sum(p[3] for p in products)
print(f'\nCustomer name = {customer_name}\n')

for i,product in enumerate(products,start=1):
    print(f'{i}. Product = {product[0]}, Price = {product[1]} ks, Quantity = {product[2]}, Total = {product[3]} ks')

print(f'\nSub total = {sub_total} ks.')

while True:
    tax_amount = input("\nTax amount in % : ")
    try:
        tax_amount = float(tax_amount)
        if 0 < tax_amount < 101:
            break
        else:
            print("Tax % must between 1 to 100!")
    except ValueError:
        print("Tax amount must be integer or float!")


tax = round(((tax_amount / 100) * sub_total), 2)
grand_total = sub_total + tax

print(f'\nTax amount = {tax} ks.')
print(f'Grand total = {grand_total} ks.')


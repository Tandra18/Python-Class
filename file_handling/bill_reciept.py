from fpdf import FPDF
import re

customer_name = input("Enter customer name : ").title().strip()
products = []

while True:
    product_name = input("\nEnter product name (or) press Enter to finish : ").title().strip()
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

#PDF generation
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial','B',16)
pdf.cell(200,10,"BILLING RECEIPT",ln=True,align='C')

pdf.set_font('Arial','',12)
pdf.cell(100,10,f"Customer name : {customer_name}", ln=True)
pdf.ln(5)

#Table header
pdf.set_font('Arial','B',12)
pdf.cell(60,10,"Product Name",1)
pdf.cell(40,10,"Quantity",1)
pdf.cell(40,10,"Unit Price",1)
pdf.cell(40,10,"Total",1)
pdf.ln()

#Table rows
pdf.set_font('Arial','',12)
for product_name,qty,price,total in products:
    pdf.cell(60,10,product_name,1)
    pdf.cell(40, 10, f"{price:.2f}", 1)
    pdf.cell(40,10,str(qty),1)
    pdf.cell(40,10,f"{total:.2f}",1)
    pdf.ln()

#Totals
pdf.ln(5)
pdf.cell(130,10,"Sub Total",0)
pdf.cell(40,10,f"{sub_total:.2f}",0,ln=True)
pdf.cell(130,10,f"Tax {tax_amount}% ",0)
pdf.cell(40,10,f"{tax:.2f}",0,ln=True)
pdf.set_font('Arial','B',12)
pdf.cell(130,10,"Grand Total",0)
pdf.cell(40,10,f"{grand_total:.2f}",0,ln=True)

#Save pdf
file_customer_name = re.sub(r'[\\/*?:#$^!@%&"<>| ]','_', customer_name)
pdf_file_name = f"{file_customer_name.lower()}_receipt.pdf"
pdf.output(pdf_file_name)
print("Receipt saved as 'billing_receipt.pdf")


















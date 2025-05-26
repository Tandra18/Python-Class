from fpdf import FPDF

# Input customer name
customer = input("Enter customer name: ")

# Input products
products = []
while True:
    name = input("Enter product name (or press Enter to finish): ")
    if name == "":
        break
    qty = int(input("Quantity: "))
    price = float(input("Unit Price: "))
    total = qty * price
    products.append((name, qty, price, total))

# Subtotal, Tax, Total
subtotal = sum([p[3] for p in products])
tax = round(subtotal * 0.05, 2)
grand_total = subtotal + tax

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "BILLING RECEIPT", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.cell(100, 10, f"Customer: {customer}", ln=True)
pdf.ln(5)

# Table Header
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Product", 1)
pdf.cell(30, 10, "Qty", 1)
pdf.cell(40, 10, "Unit Price", 1)
pdf.cell(40, 10, "Total", 1)
pdf.ln()

# Table Rows
pdf.set_font("Arial", '', 12)
for name, qty, price, total in products:
    pdf.cell(60, 10, name, 1)
    pdf.cell(30, 10, str(qty), 1)
    pdf.cell(40, 10, f"{price:.2f}", 1)
    pdf.cell(40, 10, f"{total:.2f}", 1)
    pdf.ln()

# Totals
pdf.ln(5)
pdf.cell(130, 10, "Subtotal", 0)
pdf.cell(40, 10, f"{subtotal:.2f}", 0, ln=True)
pdf.cell(130, 10, "Tax (5%)", 0)
pdf.cell(40, 10, f"{tax:.2f}", 0, ln=True)
pdf.set_font("Arial", 'B', 12)
pdf.cell(130, 10, "Grand Total", 0)
pdf.cell(40, 10, f"{grand_total:.2f}", 0, ln=True)

# Save
pdf.output("billing_receipt.pdf")
print("Receipt saved as 'billing_receipt.pdf'")

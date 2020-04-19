## Totals calculation
amount = float(input("How much did you spent today, in £ ?\n"))
vat = 20
vat_amount = (amount / 100) * vat
print("The total amount of VAT within your spend was £" + (str(vat_amount)))
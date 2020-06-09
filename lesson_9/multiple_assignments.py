## Multiple Assignments
# In python you can assign values to multiple variables in single line of code e.g.

x, y = 10, 30

print(x) # 10
print(y) # 30

# The same can be done with functions but won't cover that for now.

## Unpacking
# The following are all the same

x, y = 10, 30
x, y = (10, 30) # Tuple (immutable ie can't be changed by code other than manually)
(x, y) = 10, 30
(x, y) = (10, 30)


# As the below has 2 variable is expecting 2 parameters on the right so python will
# natively upack (split) it into the individual variables.

x, y =  "hi"
print(x) # h
print(y) # i

## Returning multiple variables
# example, in of itself not useful in this format, see next example ..

def my_function():
    return 10, 20, 30

x, y, z = my_function()

# x = 10
# y = 20
# z = 30

def order_total(subtotal):
    vat = 0.20 # 20%
    vat_amount = subtotal * vat
    total = subtotal + vat_amount

    return (total, vat_amount, vat) # Tuple that returns 3 values, comma separated

# total = total, tax = vat_amount, vat = vat below from above function
total, tax , vat = order_total(10.00) # Pass subtotal of 10 to function

# total = 12
# tax = 2.0
# vat = 0.2



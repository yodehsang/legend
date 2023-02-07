name = input("Name? \n")
price = float(input("Price of goods\n"))
tax = float(input("tax percent\n"))
amount = price * tax / 100
totalamount = price + amount
print("HI " + name + ", the total amount to pay is RM" + str(totalamount) + ", the sales tax is " + str(tax) + " percent")

name = "Sang"

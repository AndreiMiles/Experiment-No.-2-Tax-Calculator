def calculate_tax(cash):
    if cash <= 250000:
        pay = cash 
    elif cash > 250000 and cash <= 400000:
        pay = (cash - 250000) * 0.15
    elif cash > 400000 and cash <= 800000:
        pay = 22500 + (cash - 400000) * 0.2
    elif cash > 800000 and cash <= 200000:
        pay = 102500 + (cash - 800000) * 0.25
    elif cash > 2000000 and cash <= 8000000:
        pay = 402500 + (cash - 2000000) * 0.3
    elif cash > 8000000:
        pay = 2205000 + (cash - 800000) * 0.35
    else:
        print("Not a valid input, Please try again")

    return (pay)


income = float(input("Enter monthly income: "))
annual = income * 12
taxrate = calculate_tax(annual)



print("Your Yearly pay", annual) 
print("Your monthly pay", income)
print("Your Taxes", taxrate)
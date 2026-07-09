p = float(input("Enter Principle Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time: "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest:", ci)
print("Total Amount:", amount)
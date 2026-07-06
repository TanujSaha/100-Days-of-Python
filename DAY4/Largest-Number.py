a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a > b and b > c:
    print("Largest Number:", a)
elif b > a and a > c:
    print("Largest Number:", b)
else:
    print("Largest Number:", c)


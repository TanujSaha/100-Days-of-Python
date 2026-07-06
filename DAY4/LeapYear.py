year = int(input("Enter a YEAR: "))

if year % 400 == 0:
    print("It's a Leap year")
elif year % 100 == 0:
    print("It's not a Leap year")
elif year % 4 == 0:
    print("It's a Leap year")
else:
    print("It's not a Leap year")



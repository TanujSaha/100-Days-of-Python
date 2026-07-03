arr = [26, 66, 86, 75, 99]

key = int(input("Enter the element to search: "))

found = False

for num in arr:
    if num == key:
        found = True
        break

if found:
    print("Element found in the array.")
else:
    print("Element not found in the array.")   

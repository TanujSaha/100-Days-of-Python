arr = [26, 66, 86, 75, 99]

key = int(input("Enter the element to search: "))

index = -1

for i in range(len(arr)):
    if arr[i] == key:
        index = i
        break

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in the array.")



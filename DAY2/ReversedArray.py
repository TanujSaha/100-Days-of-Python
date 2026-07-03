arr = [26, 66, 86, 75, 99]

reverse = []

for i in range(len(arr)-1, -1, -1):
    reverse.append(arr[i])

print("Original array:", arr)
print("Reversed array:", reverse)
arr = [10, 20, 10, 30, 20, 40]

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Original Array:", arr)
print("New Array:", unique)
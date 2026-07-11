arr = [1, 2, 3, 4, 5, 2, 6, 1, 7, 9, 3]

duplicate = []

for num in arr:
    if arr.count(num) > 1 and num not in duplicate:
        duplicate.append(num)

print ("duplicate Numbers:", duplicate)
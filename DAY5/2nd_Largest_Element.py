arr = [20, 16, 12, 18, 14]

max = arr[0]
sec = arr[-1]

for num in arr:
    if num > max:
        sec = max
        max = num

    elif num > sec and num != max:
        sec = num

print ("Second Largest Element:", sec)
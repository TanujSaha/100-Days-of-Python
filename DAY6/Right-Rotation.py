arr = [100, 200, 300, 400, 500, 600, 700, 800]

last = arr[len(arr)-1]

for i in range (len(arr)-1, 0, -1):
    arr[i] = arr[i-1]

arr[0] = last

print("Left Rotation:", arr)
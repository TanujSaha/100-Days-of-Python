arr = [100, 200, 300, 400, 500, 600, 700, 800]

first = arr[0]

for i in range (len(arr)-1):
    arr[i] = arr[i+1]

arr[len(arr)-1] = first

print("Left Rotation:", arr)
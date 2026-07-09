arr = [0, 20, 0, 0, 30, 0, 40, 10, 0]

result = []

for num in arr:
    if num != 0:
        result.append(num)

while len(result) < len(arr):
    result.append(0)

print("Result:", result)
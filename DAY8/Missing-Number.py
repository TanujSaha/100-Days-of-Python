arr = [1, 2, 3, 4, 5, 6, 7, 9, 10]

n = 10

for i in range(1, n+1):
    if i not in arr:
        print("Missing value:", i)

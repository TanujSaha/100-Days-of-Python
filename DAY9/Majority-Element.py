#Majority Logic - An element appearing more than n/2 times.

arr = [1,2,3,2,4,2,5,6,2,7,2,2]

majority = None

for num in arr:
    if arr.count(num) > len(arr) // 2:
        majority = num
        break

if majority != None:
    print("Majority Number:", majority)

else:
    print("No Majority Number")
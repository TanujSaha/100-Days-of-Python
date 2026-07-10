arr = [10, 20, 10, 30, 20, 10]

checked = []

for num in arr:
    if num not in checked:
        count = 0

        for item in arr:
            if item == num:
                count += 1

        print(num, "occurs", count, "times")
        checked.append(num)
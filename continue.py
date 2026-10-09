data = [1, -1, 2, 3]

total = 0
for x in data:
    if x < 0:
        continue
    total += x

print(total)
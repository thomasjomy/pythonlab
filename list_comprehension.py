values = [1, 2, 3, 4]
squares = [v * v for v in values]
evens = [v for v in values if v % 2 == 0]
print(squares)
print(evens)
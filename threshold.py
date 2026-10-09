price = 105
threshold = 100

if price > threshold:
    status = "above"
elif price == threshold:
    status = "equal"
else:
    status = "below"

print(status)
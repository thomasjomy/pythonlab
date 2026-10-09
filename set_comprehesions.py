raw_symbols = ["aapl", "AAPL", "msft", "MSFT"]
canonical = {s.upper() for s in raw_symbols}
print(canonical)
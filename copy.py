import copy

positions = [{"symbol": "AAPL", "qty": 10}]
shallow = positions.copy()
deep = copy.deepcopy(positions)

positions[0]["qty"] = 20
print(shallow)
print(deep)
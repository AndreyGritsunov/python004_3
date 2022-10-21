n = [1.1, 1.2, 4, 10.01]
b = []
for i in n:
    if isinstance(i, float):
        b.append(i - int(i))
print(max(b)-min(b))
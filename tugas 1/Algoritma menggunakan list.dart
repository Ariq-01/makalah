data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
hasil = []

for item in data:
    if item not in hasil:
        hasil.append(item)
print(hasil)
data = [232, 23, 2, 3, 2, 3]
hash = []
for item in data:
    if item not in hash:
        hash.append(item)
print(hash)

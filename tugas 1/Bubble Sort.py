angka = [465,747,7,87,87,7,8,78,78,78,77,8]
for i in range(len(angka)):
    for j in range(len(angka)-i-1):
        if angka[j] < angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]
    print(angka)
print(angka)

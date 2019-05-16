count = int(input("Adet giriniz: "))
dizi = []

for i in range(count):
    dizi.append(int(input(str(i+1) + ". sayi: ")))

for i in range(len(dizi)-1):
    for j in range(len(dizi)-1):
        if(dizi[j] > dizi[j+1]):
            temp = dizi[j]
            dizi[j] = dizi[j+1]
            dizi[j+1] = temp

print(dizi)
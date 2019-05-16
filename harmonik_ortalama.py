count = int(input("Adet giriniz: "))
dizi = []

for i in range(count):
    dizi.append(int(input(str(i+1) + ". sayi: ")))

toplamlar = 0

for sayi in dizi:
    toplamlar += 1 / sayi

sonuc = count / toplamlar
print(sonuc)
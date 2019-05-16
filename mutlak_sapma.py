count = int(input("Adet giriniz: "))
dizi = []
toplamlar = 0

for i in range(count):
    dizi.append(int(input(str(i+1) + ". sayi: ")))

for x in range(count):
    sayi = dizi[x]
    toplamlar += sayi

aritmatik_ort = toplamlar / count

ust = 0
for i in dizi:
    ust += ((aritmatik_ort-i) ** 2)**(1/2)

sonuc = (ust/count)
print(sonuc)
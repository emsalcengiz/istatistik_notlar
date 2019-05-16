count= int(input("Adet giriniz: "))
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
    ust += (i-aritmatik_ort) ** 3

sonuc = (ust/(count-1))
print(sonuc)
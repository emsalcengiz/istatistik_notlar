count = int(input("Adet giriniz: "))
dizi = []
toplam = 0

for i in range(count):
    sayi = int(input(str(i+1) + ". sayi: "))
    dizi.append(sayi)
    toplam += sayi

print("Aritmatik ortalama: ", toplam/count)
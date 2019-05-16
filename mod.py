count = int(input("Adet giriniz: "))
dizi1 = []
dizi2 = []

for i in range(count):
    dizi1.append(int(input(str(i+1) + ". sayi: ")))

for i in range(len(dizi1)-1):
    for j in range(len(dizi1)-1):
        if(dizi1[j] > dizi1[j+1]):
            temp = dizi1[j]
            dizi1[j] = dizi1[j+1]
            dizi1[j+1] = temp

maks = -1

for i in range(count):

    if i-1 == count:
        sonraki = dizi1[i+1]
    else:
        sonraki = None

    if(dizi1[i] != sonraki):
        if(maks == dizi1.count(dizi1[i])):
            dizi2.append(dizi1[i])
        elif(maks < dizi1.count(dizi1[i])):
            dizi2.clear()
            dizi2.append(dizi1[i])
            maks = dizi1.count(dizi1[i])

dizi2 = list(set(dizi2))
print(dizi2)
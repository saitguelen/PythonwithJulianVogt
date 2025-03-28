
# Multiplikation
#
# Schreibe ein Programm, das ermittelt,
# wie viele ganzzahlige Multiplikator-Multiplikand-Kombinationen
# vom Produkt 8.420.000 es gibt,
# bei denen sowohl Multiplikator, als auch Multiplikand
# kleiner als 10.000 sind.
#
# 1000*8420 und 8420*1000 zählt nur einmal.


ziel=8420000 #Unsere Ziel
#nun mache ich eine ForSchleife
zaehler=0

listi=[]
for i in range(1,10000):  #10.000’den küçük çarpanlar arıyoruz.
    if ziel%i==0: #Bir sayı, 8.420.000'ü tam bölüyorsa o bir çarpandır.
        j=ziel//i

        if j<=10000:  #Adım 4: Her iki çarpan da 10.000’den küçük mi?
            if i<=j:  #Adım 5: Çiftleri tekrar saymamak için
                listi.append(i)
                zaehler +=1

print("Anzahl der gültigen Kombinationen: ",zaehler)

print(f"carpanlar: {listi}")
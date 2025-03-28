
# Zweierschritte

# Schreibe ein Programm, das zwei Zahlen vom Anwender abfragt.
# Das Programm soll nun eine Funktion aufrufen,
# die die Werte von der ersten bis zur zweiten Zahl in Zweierschritten ausgibt.
# Für diese Ausgabe müssen zwei verschiedene Optionen bestehen.
# Je nachdem, ob die erste oder die zweite Zahl größer ist.

# Z.B.:
# 3-9 -> 3 5 7 9
# 18-12 -> 18 16 14 12


def zweierschritte():
    zahl_1 = int(input("Geben Sie erste Zahl ein: "))
    zahl_2 = int(input("Geben Sie zweite Zahl ein: "))

    if zahl_1<zahl_2:
        for i in range(zahl_1,zahl_2+1,2):
            print(i, end=" ")
    else:
        for i in range(zahl_1,zahl_2-1,-2):

            print(i, end=" ")
    print()


zweierschritte()

"""
def zweierschrittee():
    liste=[]
    z1 = int(input("Geben Sie erste Zahl ein: "))
    z2 = int(input("Geben Sie zweite Zahl ein: "))

    if z1<z2:
        for i in range(z1,z2+1,2):
            liste.append(i)
    else:
        for i in range(z1,z2-1,-2):

            liste.append(i)
    return liste

# Kullanıcıdan değer al
z1 = int(input("Erste Zahl: "))
z2 = int(input("Zweite Zahl: "))

# Fonksiyonu çağır ve sonucu al
liste = zweierschrittee(z1, z2)

# Sonucu ekrana yazdır
print("Zweierschritte:", liste)

"""
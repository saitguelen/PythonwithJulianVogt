
# Potenzen von Zwei
#
# Schreibe ein Programm, das alle Potenzen von 2 ausgibt
# deren Ergebnis kleiner als 10.000 ist.
# Hilfsmittel: Schleife, **
#
# Zusatz: Die Ausgabe soll folgendermaßen aussehen:
# 2 ** 0 = 1
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8
# 2 ** 4 = 16
# 2 ** 5 = 32
# 2 ** 6 = 64
# ...
k=2

for i in range(0,10000):
    ergebnis= k**i
    if ergebnis>10000:
        break
    print(f"{k} ** {i} = {ergebnis}")
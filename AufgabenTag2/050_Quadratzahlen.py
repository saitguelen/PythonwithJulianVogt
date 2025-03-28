
# Quadratzahlen

"""
Schreibe ein Skript, welches alle Quadratzahlen von natürlichen
Zahlen (1, 2, 3, ...) ausgibt, die kleiner als 100 sind.
(Die Quadratzahlen sollen kleiner 100 sein!)

Zusatz: Gib auch die Anzahl der gefundenen Quadratzahlen aus
"""
for i in range(1,10):
    QuadratZahlen= i*i
    print(QuadratZahlen, end=" ")

zahl=0
while zahl**2<100:
    print(zahl, zahl**2)
    zahl +=1






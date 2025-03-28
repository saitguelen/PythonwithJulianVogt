
# Zwei Zahlen genau vergleichen

# Schreibe ein Programm, das testet und ausgibt,
# welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.
# Die beiden Zahlen sollen zufällig erzeugt werden.
import random

zahl1=random.randint(1,50)
zahl2=random.randint(1,50)
print(zahl1)
print(zahl2)

if zahl1==zahl2:
    print("Die Zahlen sind Gleich")

elif zahl1>zahl2:
    print("Zahl1 ist größer als Zahl2")

else:
    print("Zahl2 ist größer als Zahl1")


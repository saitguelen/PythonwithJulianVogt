
# Portokosten

"""
Die Portokosten (Versandkosten) sind wie folgt festgelegt:
 0 - 39.99 € Bestellwert kosten 3.99 € Porto
40 - 69.99 € Bestellwert kosten 2.99 € Porto
70 - 99.99 € Bestellwert kosten 1.99 € Porto
ab 100 € ist portofrei

Es soll eine Zufallszahl (bestellwert)
von 1.00 - 130.00 erzeugt werden (z.B. 40.47, 123.78)

Dann soll ermittelt werden,
wie hoch die entsprechenden Portokosten sind.
Am Ende sollen der Bestellwert, die Portokosten
und der Gesamtbetrag ausgegeben werden.
"""
import random

Bestellwert = round(random.uniform(1.00,130.00),2)

if Bestellwert<40.00:
    Porto=3.99


elif Bestellwert<70.00:
    Porto=2.99


elif Bestellwert<100.00:
    Porto=1.99


else:
    Porto=0.00


Gesamt = round(Bestellwert + Porto, 2)

print("Bestellwert:", Bestellwert, "€")
print("Portokosten:", Porto, "€")
print("Gesamtbetrag:", Gesamt, "€")



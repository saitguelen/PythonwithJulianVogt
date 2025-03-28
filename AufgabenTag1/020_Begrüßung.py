
# Begrüßung

# Es soll eine Begrüßung in Abhängingkeit zur Uhrzeit ausgegeben werden.

# Zwischen 22Uhr und 5Uhr: Gute Nacht
# Vor 11Uhr: Guten Morgen
# Vor 15Uhr: Mahlzeit
# Vor 18Uhr: Guten Nachmittag
# Vor 22Uhr: Guten Abend

# Benutze zum Testen randint(0, 23),
# um eine Zahl von 0 bis 23 zu erzeugen.
import random

Uhr=random.randint(0,23)

print(Uhr)

if 22 <= Uhr or Uhr <= 5:
    print("Gute Nacht")
elif Uhr < 11:
    print("Guten Morgen")
elif Uhr < 15:
    print("Mahlzeit!!")
elif Uhr < 18:
    print("Guten Nachmittag!!")
else:
    print("Guten Abend!!")


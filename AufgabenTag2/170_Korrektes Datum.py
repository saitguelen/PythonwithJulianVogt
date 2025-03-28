
# Korrektes Datum

"""
Die Meyer GmbH benötigt ein Modul,
das ein Datum auf Korrektheit prüft.
Ist das zu prüfende Datum korrekt,
so ist die Variable datok auf 1, andernfalls auf 0
zu setzen.

Beispiele:

29.02.1999 - datok: 0
29.02.2000 - datok: 1
13.05.2000 - datok: 1
32.05.2000 - datok: 0
24.13.2000 - datok: 0

Für die Jahre gilt: jahr > 1900 UND jahr < 2100
"""

jahr = int(input("Geben Sie bitte Jahr ein: "))
monat = int(input("Geben Sie bitte Monat ein: "))
tag = int(input("Geben Sie bitte Tag ein: "))

datok = 0

if jahr <= 1900 or jahr >= 2100:
    print("Ungültiges Jahr")
else:
    if monat < 1 or monat > 12:
        print("Ungültiger Monat")
    else:
        # Schaltjahr prüfen
        if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
            februar = 29
        else:
            februar = 28


        tage_pro_monat = [31, februar, 31, 30, 31, 30,
                          31, 31, 30, 31, 30, 31]


        if 1 <= tag <= tage_pro_monat[monat - 1]:
            datok = 1
        else:
            print("Ungültiger Tag")

print(" Datok:", datok)

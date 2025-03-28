
# Teilersumme

"""
Schreibe eine Funktion, die überprüft, ob bei einer Zahl
die Summe aller Teiler kleiner als die Zahl ist.
Die Zahl selber soll hierbei nicht zu den Teilern zählen.

Bei 81 würde True zurück gegeben werden, da
1 + 3 + 9 + 27 = 40
und 40 < 81

Bei 80 würde False zurück gegeben werden, da
1 + 2 + 4 + 5 + 8 + 10 + 16 + 20 + 40 = 106
und 106 > 80
"""


def teilersumme(zahl):
    summe = 0
    teiler=[]
    for i in range(1,zahl):
        if zahl%i==0:
            summe +=i
            teiler.append(str(i))
    rechnung= "+".join(teiler)
    print(f"{rechnung} = {summe}")
    print()
    if summe < zahl:
        return f"Bei {zahl}  würde True zurück gegeben werden, da {rechnung} = {summe}, Summe = {summe} und {summe} < {zahl}"
    else:
        return f"Bei {zahl} würde False zurück gegeben werden, da  {rechnung} = {summe}, Summe = {summe} und {summe} ≥ {zahl}"


print(teilersumme(65))
print(teilersumme(165))
print(teilersumme(90))
print(teilersumme(81))
print(teilersumme(80))


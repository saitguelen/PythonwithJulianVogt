
# Einmaliges in einer Liste

"""
Schreibe eine Funktion,
die eine Liste mit neun zufälligen Zahlen befüllt und zurück gibt.
Dabei sollen vier Zahlen doppelt vorkommen und eine Zahl nur einmal.

Dann mische die Liste per random.shuffle() und schreibe eine zweite Funktion,
die aus dieser Liste die Zahl findet, die nur einmal vorkommt.
"""

import random

def zufalls_liste():
    doppelte=random.sample(range(1,100),4)  #sample kullanma nedeni bir sayi bir kere gelsin
    liste=doppelte*2   #her elemani iki kere carpar listede 8 eleman olur
    einmalig= random.choice([x for x in range(1,100) if x not in doppelte]) ## 9. elemani buradan aliriz
    liste.append(einmalig)
    random.shuffle(liste)

    return liste

def finde_einmalige_zahl(liste):
    for zahl in liste:
        if liste.count(zahl)==1:
            return zahl


liste = zufalls_liste()
print("Gemischte Liste:", liste)

einzig = finde_einmalige_zahl(liste)
print("Einmalige Zahl ist:", einzig)


# Doppelte Zahl

"""
Schreibe ein Funktion, die überprüft,
ob in einer Liste mit Zahlen zwei Zahlen gleich sind.
Der Funktion wird die Liste übergeben
und sie soll True zurück geben, wenn es Doppelte gibt
und ansonsten soll die Funktion False zurück geben.
"""

def doppelte_zahl(liste):
    gesehen=set()
    for zahl in liste:
        if zahl in gesehen:
            return True
        gesehen.add(zahl)
    return False


print(doppelte_zahl([1,2,3,4]))  #Ausgabe: False
print(doppelte_zahl([1, 2, 3, 4]))       # False
print(doppelte_zahl([5, 6, 7, 5]))       # True
print(doppelte_zahl([10, 20, 30, 10]))   # True



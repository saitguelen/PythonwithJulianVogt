
# Min-Max-Funktion

# Die in Python vordefinierten Funktionen min() und max() ermitteln
# das kleinste bzw. größte Element einer Liste von Zahlen.
# Programmiere die Funktion min_max(),
# die die beiden entsprechenden Elemente als Tupel zurückgibt,
# ohne auf min() und max() zurückzugreifen.

def minmax(liste):
    min=liste[0]
    max=liste[0]
    for wert in liste:
        if wert<min:
            min=wert
        if wert>max:
            max=wert
    return min,max

print(minmax([12,15,14,15,12,10,20,23,36,56,89,94]))
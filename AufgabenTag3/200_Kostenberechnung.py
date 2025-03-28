
# Kostenberechnung

"""
Erstelle eine Funktion zur Kostenberechnung.
Dieser wird Preis, Anzahl und Währung als Argumente übergeben
und sie soll daraus die Kosten berechnen und zurück geben.
Standardmäßig soll die Anzahl 100 betragen
und die Währung Euro sein.
"""


#preis=int(input("Geben Sie Preis ein: "))
#anzahl=int(input("Standardmäßig soll die Anzahl 100 betragen aber Sie können andere Anzahl eingeben: "))
def kostenberechnung(preis,anzahl=100,waehrung="€"):
    kosten=preis*anzahl
    return f"Kosten: {kosten:.2f} {waehrung}"

print(kostenberechnung(3.0,250))
print(kostenberechnung(6))
print(kostenberechnung(25.25,250))
#print(kostenberechnung(preis, anzahl))
######Tenärer Operator

"""
Was ist der ternäre Operator?
(Türkisch: üçlü operatör)

Der ternäre Operator erlaubt dir, kurz und knapp eine if-else-Bedingung in einer Zeile zu schreiben.

👉 Er ist perfekt für einfache Entscheidungen.

🧠 Merksatz:
if önce gelir!

else kısmı mutlaka olmalı

Nur für einfache Entscheidungen (nicht für komplexe Bedingungen mit vielen elif!)

Ternary operator, if-else yapısını tek satırda yazmamıza olanak tanır:

sonuc = "Doğruysa bu" if koşul else "Yanlışsa bu"

java: i= Bedingung ? wertenwaht : wertenfalsch

python: wertenwahr if bedingung else wertenfalsch

"""

zahl = 7
ergebnis = "gerade" if zahl % 2 == 0 else "ungerade"
print(ergebnis)
# Ausgabe: ungerade
print("#############################################################")
alter = 20

status = "Volljährig" if alter >= 18 else "Minderjährig"

print(status)
# Ausgabe: Volljährig

########################     LISTEN           ####################

"""

Eine Liste ist eine geordnete Sammlung von Elementen, die:

verschiedene Datentypen enthalten kann,

veränderbar (mutable) ist,

über den Index erreichbar ist (Index beginnt bei 0).

Liste: Python'da birden fazla değeri bir arada tutan yapılardır.

[ ] köşeli parantezle yazılır.

append(), insert(), remove() gibi metotlarla yönetilir.

Sıralıdır (index'le erişilir) ve değiştirilebilir (mutable)
"""

########## Liste Erstellen

zahlen = [1, 2, 3, 4, 5]
namen = ["Anna", "Ben", "Chris"]
gemischt = [1, "Hallo", True, 3.14]


### Elemente einer Liste ansprechen

print(zahlen[0])   # 1
print(namen[2])    # "Chris"

##############    Elemente ändern

zahlen[0] = 100
print(zahlen)      # [100, 2, 3, 4, 5]

############    ➕ Elemente hinzufügen

zahlen.append(6)           # fügt am Ende an
zahlen.insert(2, 99)       # fügt 99 an Position 2 ein

############# ➖ Elemente entfernen

zahlen.remove(3)           # entfernt den Wert 3
zahlen.pop(1)              # entfernt Element an Index 1
#zahlen.pop()             ##entfernt letzte Element
################# 🔁 Liste durchlaufen (Schleife)
print()
for name in zahlen:
    print(name, end=" ")
print()
##############  Länge einer Liste
print("Length für zahlen: ",len(zahlen))  # Anzahl der Elemente

#################### Sortieren

#Die sort() methode sortiert die werte aufsteigend, mit reverse() die werte umgekehrt werden können
print(zahlen)
print()

zahlen.sort()              ######## sortiert die werte aufsteigend

print(zahlen)

zahlen.reverse()      ###### die werte umgekehrt werden können
print(zahlen)

############# Jagged 2D Array (Array von Arrays)

# Die verschachtelnen Listen können unterschiedliche Liste erstellen

tabelle = [
    [1,2,3,4],[45,48,43],[7,8,9,4,56,42,14]
]
print(tabelle[0])   #Ausgabe: [1, 2, 3, 4]
tabelle[2].reverse()
tabelle[1].sort()
print(tabelle)   ##Ausgabe:  [[1, 2, 3, 4], [43, 45, 48], [14, 42, 56, 4, 9, 8, 7]]

hochdimensionaler_tensor= [[[[45,42]]]]

print(hochdimensionaler_tensor[0][0][0][0])  #Ausgabe: 45

print(hochdimensionaler_tensor[0][0][0][1])   #Ausgabe: 42

######### Und können wir eine Copy an einer Liste erstellen

kopie1= zahlen.copy()  #Ausgabe: [100, 99, 6, 5, 4]
print(kopie1)

kopie1[2]=25
print(kopie1)  #Ausgabe: [100, 99, 25, 5, 4]
## so wie Liste können wir eine element zuweisen, löschen, hinzufügen, umgekehrte liste erstellen usw.
kopie1.append(12)
kopie1.pop()
kopie1.reverse()
print(kopie1)
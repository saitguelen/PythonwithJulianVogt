############Continue und Break

"""
🔄 Was sind continue und break?
Beide werden in Schleifen (z. B. for oder while) verwendet:

Befehl	                Bedeutung (Deutsch)	             Wirkung
break	                Schleife sofort beenden	         verlässt die Schleife vollständig
continue	            aktuelle Runde überspringen	     geht direkt zum nächsten Durchlauf
🧠 Merksätze:
break → Schleife beenden

continue → Diese Runde überspringen, weiter mit der nächsten

"""

#####################  Break

zahlen = [1, 3, 5, 7, 9, 10, 11]

for zahl in zahlen:
    if zahl == 10:
        print("🔴 Zahl 10 gefunden! Schleife wird beendet.")
        break
    print("Zahl:", zahl)

i=0
summe=0
while i<len(zahlen):
    summe += zahlen[i]
    i +=1
print(summe)  #Ausgabe: 46

##################  Continue

for i in range(1, 6):
    if i == 3:
        print("⏭️ Drei wird übersprungen.")
        continue
    print("Zahl:", i)
summe1=1
summe2=0
for i in range(1,10):
    if i%2==0:
        summe1 *=i  #Ausgaabe 384
    else:
        summe2 +=i   #Ausgabe:25

print(summe1)
print(summe2)


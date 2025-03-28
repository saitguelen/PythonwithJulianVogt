
# Teilbar
#
#  Schreibe ein Skript, das alle Zahlen von 1 bis 100 ausgibt,
#  die durch drei teilbar sind.
#  Hilfsmittel: Schleife, if, Modulo
#
#  Zusatz 1: Gib die Anzahl der Zahlen aus.
#
#  Zusatz 2: Das Programm soll nun alle Zahlen ausgeben,
#            die durch 3 ODER 7 teilbar sind.
#            Gib auch hiervon die Anzahl aus.

for i in range(1,100):
    if i%3==0:
        print(i,end=" ")

print()

count=0
for j in range(1,100):
    if j%3==0 or j%7==0:
        print(j,end=" ")
        count +=1

print()
print("Es gibt durch 3 oder durch 7 teilbar Zahlen: ", count)












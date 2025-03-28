
# Fibonacci

"""
Schreibe ein Programm, das per for-Schleife die ersten 10 Zahlen der
Fibonacci-Folge ausgibt: 0 1 1 2 3 5 8 13 21 34
Die ersten beiden Zahlen dürfen hardcodiert ausgegeben werden:
print(0, 1)
Alle folgenden Zahlen müssen dann in der for-Schleife ausgegeben werden.
Die Fibonacci-Folge beginnt mit 0 und 1.
Ab dann entsteht die folgende Zahl immer
indem man jeweils die beiden vorherigen Zahlen addiert.

Zusatz: Gib alle Fibonacci Zahlen unter 500 aus
"""
print(0, 1, end=" ")
a, b = 0, 1

for _ in range(8):  # 2 sayı zaten yazdırıldı, 10-2=8 kaldı
    a, b = b, a + b
    print(b, end=" ")


a, b = 0, 1
print("\nFibonacci-Zahlen unter 500:")

while a < 500:
    print(a, end=" ")
    a, b = b, a + b

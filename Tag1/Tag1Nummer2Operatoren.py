#Aritmetischen Operatoren

"""
📌 Erklärungen mit Beispielen:
+ Addition → 5 + 3 = 8

- Subtraktion → 7 - 2 = 5

* Multiplikation → 4 * 3 = 12

/ Division → 9 / 2 = 4.5 (immer ein float!)

// Ganzzahldivision → 9 // 2 = 4 (ohne Nachkommastelle)

% Modulo (Rest) → 9 % 2 = 1 (Rest der Division)

** Potenzierung → 2 ** 4 = 16 (also 2⁴)

🧠 Merktipp:
/ → normale Division mit Komma

// → Division ohne Komma (abgeschnitten)

% → Rest wie beim Teilen in der Schule

** → wie mathematisches "hoch"

"""

"""
Es gilt:
--Ist mindestens einer der Operanden ein Float, ist auch das Ergebnis des Ausdrucks ein Float
        --Ausnahme : '/' ist immer ein float
--Punkt vor Strich: '2+3*3'=11
--Exponentiation(hoch rechnen) vor Punkt: 2*3**2=18
--Klammern immer zuerst:3*(2+3)=15
--Die meisten Operatoren sind "linksassoziativ": 12/3*4=8 nicht 1!!
--Beispiel
"""

print(4**3**2)
print((4**3)**2)
print(2**2+2)
print(2**16**0)
print("############################################################")
#############################

###Binäre Operatoren

"""
🧮 Binäre Operatoren (Bitweise Operatoren)
Binäre (bitweise) Operatoren arbeiten nicht auf ganzen Zahlen direkt, sondern auf deren binärer Darstellung (also auf den einzelnen Bits: 0 und 1).

👉 Sie vergleichen oder manipulieren Zahlen Bit für Bit.

🧠 Merksätze:
& = nur wenn beide 1 → Ergebnis 1

| = wenn mindestens einer 1 → Ergebnis 1

^ = wenn genau einer 1 → Ergebnis 1

~ = alles umkehren

<< = mal 2, >> = geteilt durch 2


"""
print("Binär")
a = 5     # binär: 0101
b = 3       # binär: 0011

print(a & b)   # 1  → 0101 & 0011 = 0001
print(a | b)   # 7  → 0101 | 0011 = 0111
print(a ^ b)   # 6  → 0101 ^ 0011 = 0110 XOR
print(~a)      # -6 → Bitweise Negation (Zweierkomplement)
print(a << 1)  # 10 → 0101 wird zu 1010 (nach links verschoben)Her adımda ×2
print(a >> 1)  # 2  → 0101 wird zu 0010 (nach rechts verschoben)Her adımda tam bölme (//2)
print("############################################################")
print(0b00000000001<<3) #2
print(0b10001>>3)#8
print(0b1001<<3) #72
print(0b1001>>1)# 4

###############################################################
print("############################################################")
####################### Vergleichsoperatoren (Karşılaştırma Operatörleri)
"""
🔍 Vergleichsoperatoren (Karşılaştırma Operatörleri)
Mit Vergleichsoperatoren kannst du zwei Werte miteinander vergleichen.
Das Ergebnis ist immer entweder True (wahr) oder False (falsch).

Operator	Bedeutung (Deutsch)	Bedeutung (Türkisch)	Beispiel	Ergebnis
==	gleich	eşit mi?	5 == 5	True
!=	ungleich	eşit değil mi?	5 != 3	True
>	größer als	büyük mü?	10 > 5	True
<	kleiner als	küçük mü?	3 < 8	True
>=	größer oder gleich	büyük ya da eşit mi?	5 >= 5	True
<=	kleiner oder gleich	küçük ya da eşit mi?	4 <= 3	False

"""

print("############################################################")
x = 7
print(x == 7)   # True
print(x != 5)   # True
print(x > 3)    # True
print(x < 2)    # False
print(x >= 7)   # True
print(x <= 6)   # False

print("############################################################")

######🔗 Logische Operatoren (Mantıksal Operatörler)

"""
Logische Operatoren verbinden mehrere Bedingungen.
Ergebnis: True oder False

Operator	Bedeutung (Deutsch)	Bedeutung (Türkisch)	Beispiel	Ergebnis
and	und	ve	True and False	False
or	oder	veya	True or False	True
not	nicht	değil (tersi)	not True	False
"""

a = 10
b = 5

print(a > 5 and b < 10)     # True (her ikisi de doğru)
print(a < 5 or b < 10)      # True (b < 10 doğru)
print(not (a == 10))        # False (çünkü a 10 zaten)


print("############################################################")
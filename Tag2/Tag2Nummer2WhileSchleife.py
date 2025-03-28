
############# While Schleife

"""
🔄 Was ist eine while-Schleife?
Eine while-Schleife führt einen Codeblock so lange aus, wie eine Bedingung wahr (True) ist.


Regel	                        Bedeutung
Bedingung muss True sein	    Sonst wird Schleife nicht ausgeführt
break	                        Bricht die Schleife sofort ab
continue	                    Überspringt den aktuellen Durchlauf
Achtung auf Endlosschleifen!	Schleife muss irgendwann enden

Türkçe özet:
while döngüsü, koşul doğru olduğu sürece çalışır.

Örneğin: while x < 5: → x, 5’ten küçük olduğu sürece tekrarlar.

break → döngüyü durdurur.

continue → bu turu atla, bir sonrakine geç.
"""


zahl = 1

while zahl <= 5:
    print(zahl)
    zahl += 1

print()
############# Nur gerade Zahlen zählen

zahl = 0

while zahl < 10:
    zahl += 1
    if zahl % 2 != 0:
        continue
    print(zahl)

print()
#############  Unendliche Schleife mit Abbruch (break)

while True:
    eingabe = input("Gib 'stop' ein, um zu beenden: ")
    if eingabe == "stop":
        break
    print("Du hast geschrieben:", eingabe)
###########

###############  🎮 Zahl erraten – mit while-Schleife (Gizli Sayıyı Tahmin Et)

import random

# Eine geheime Zufallszahl zwischen 1 und 100
geheime_zahl = random.randint(1, 100)

versuch = 0  # wie viele Versuche?
geraten = False  # ob der Spieler richtig geraten hat?
print(geheime_zahl)
print("🔢 Ich habe eine Zahl zwischen 1 und 100 im Kopf. Kannst du sie erraten?")

while not geraten:
    eingabe = input("Dein Tipp: ")

    # prüfen ob gültige Zahl
    if not eingabe.isdigit():
        print("⚠️ Bitte gib eine gültige Zahl ein!")
        continue

    tipp = int(eingabe)
    versuch += 1

    if tipp < geheime_zahl:
        print("🔼 Zu klein!")
    elif tipp > geheime_zahl:
        print("🔽 Zu groß!")
    else:
        print(f"🎉 Richtig! Die geheime Zahl war {geheime_zahl}. Du hast {versuch} Versuche gebraucht.")
        geraten = True

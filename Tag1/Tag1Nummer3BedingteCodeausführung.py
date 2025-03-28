"""
Bedingte Codeausführung
(Türkisch: Koşullu Kod Çalıştırma)

📘 Was bedeutet „bedingte Codeausführung“?
Bedingte Codeausführung bedeutet: 👉 Ein bestimmter Teil des Codes wird nur dann ausgeführt, wenn eine bestimmte Bedingung erfüllt ist.

Stell dir vor:
„Wenn etwas wahr ist, dann mache etwas.“
(auf Englisch: "if this, then that")

🔧 Wie funktioniert das in Python?
In Python benutzt man dafür:

if

elif (else if)

else

################################################
if Bedingung:
    # dieser Code wird ausgeführt, wenn die Bedingung True ist
elif andere_Bedingung:
    # wenn die erste falsch war, aber diese richtig ist
else:
    # wenn keine Bedingung zutrifft

    📌 Was passiert hier im Hintergrund?
Der Computer prüft die erste Bedingung (if):

Ist sie wahr (True)? → Führt nur diesen Block aus.

Wenn nicht wahr, prüft er die nächste (elif).

Wenn keine if oder elif wahr ist → führt er den else-Block aus.

Nur ein einziger Block wird immer ausgeführt – der erste, dessen Bedingung True ist.

🧠 Warum wichtig?
Programme sollen intelligent reagieren können.

Z. B. Benutzerpasswörter prüfen, Menüauswahl verarbeiten, Entscheidungen treffen, ...

Ohne bedingte Ausführung wären Programme statisch und reaktionslos.

"""

alter = int(input("Geben Sie bitte Ihr Alter an: "))

if alter >= 18:
    print("Du bist volljährig.")
else:
    print("Du bist noch nicht volljährig.")

print("############################################################")
#################################################
note = int(input("Geben Sie bitte Ihre Note ein: "))

if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
else:
    print("Nicht ausreichend")
print("############################################################")

#########################################
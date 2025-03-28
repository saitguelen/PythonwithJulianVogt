from Tag3.Tag3Nummer3DatenstrukturenKombinieren import punkte


# Passwortqualität

# Schreibe eine Funktion, die die Qualität von Passwörtern nach
# einem einfachen Punktesystem bewertet.
# Es gelten dabei die folgenden
# Regeln:
# – Passwort mit 7 oder weniger Zeichen: immer 0 Punkte,
# - egal, welche Kriterien noch erfüllt sind.
# – Ab 8 Zeichen: 1 Punkt
# – Enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt
# – Enthält mehr als sechs unterschiedliche Zeichen: +1 Punkt
# – Enthält zumindest eine Ziffer: +1 Punkt
# – Enthält zumindest ein Sonderzeichen: +1 Punkt
# Beispiele:
# – 'abc': 0 Punkte
# – 'abcdefghij': 2 Punkte
# – 'ab1122$$!!': 3 Punkte
# – 'Abcd1234$!': 5 Punkte

def passwort_qualitaet(eingabe):
    punkte = 0

    if len(eingabe) <= 7:
        return 0  # direkt 0 puan verilir

    punkte += 1  # ≥ 8 karakter

    if any(c.islower() for c in eingabe) and any(c.isupper() for c in eingabe):
        punkte += 1

    if len(set(eingabe)) > 6:
        punkte += 1

    if any(c.isdigit() for c in eingabe):
        punkte += 1

    if any(not c.isalnum() for c in eingabe):  # harf ve rakam dışı bir karakter varsa
        punkte += 1

    return punkte

testliste = ['abc', 'abcdefghij', 'ab1122$$!!', 'Abcd1234$!']

for pw in testliste:
    print(f"'{pw}': {passwort_qualitaet(pw)} Punkte")







"""
def passwortqualität(s: str) -> int:
    if len(s) <= 7:
        return 0

    if s == "Correct Horse Battery Staple":
        return 1000

    grade = 1

    # – Enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt
    if any(map(str.islower, s)) and any(map(str.isupper, s)):
        grade += 1

    # – Enthält mehr als sechs unterschiedliche Zeichen: +1 Punkt
    if len(set(s)) > 6:
        grade += 1

    # – Enthält zumindest eine Ziffer: +1 Punkt
    if any(map(str.isdigit, s)):
        grade += 1

    # – Enthält zumindest ein Sonderzeichen: +1 Punkt
    if not all(map(str.isalnum, s)):
        grade += 1

    return grade
"""






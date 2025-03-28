"""
🧠 Was bedeutet „Datenstrukturen kombinieren“?
Es bedeutet, dass man verschiedene Datenstrukturen wie:

Listen (list)

Tupel (tuple)

Dictionaries (dict)

Sets (set)

miteinander verschachtelt oder zusammen verwendet.

Man kann also z.B. eine Liste von Dictionaries haben, oder ein Dictionary, das Tupel enthält

"""

#✅ 1. Liste von Dictionaries
#Eine sehr häufige Kombination z. B. bei mehreren Personen:
personen = [
    {"name": "Ali", "alter": 25},
    {"name": "Sait", "alter": 30},
    {"name": "Merve", "alter": 28}
]

print(personen[0]["name"])  # Ausgabe: Ali

#✅ 2. Dictionary mit Listen als Werte

kurse = {
    "Mathe": [90, 85, 100],
    "Deutsch": [75, 88, 92]
}

print(kurse["Mathe"])  # Ausgabe: [90, 85, 100]

#✅ 3. Dictionary mit Tupeln

orte = {
    "Berlin": (52.52, 13.405),
    "Hamburg": (53.551, 9.993)
}

print(orte["Berlin"])  # Ausgabe: (52.52, 13.405)

#✅ 4. Liste mit Tupeln

punkte = [(1, 2), (3, 4), (5, 6)]

for x, y in punkte:
    print("X:", x, "Y:", y)
"""
🧠 Warum kombiniert man Datenstrukturen?
Um komplexe Daten übersichtlich zu speichern

Für Tabellenähnliche Daten (wie in Datenbanken)

Für Objekte mit mehreren Eigenschaften (z. B. Person = Name + Alter)
"""

# Her şey bir arada

daten = [
    {
        "name": "Ali",
        "alter": 25,
        "kurse": [("Mathe", 90), ("Deutsch", 85)]
    },
    {
        "name": "Merve",
        "alter": 28,
        "kurse": [("Mathe", 95), ("Deutsch", 92)]
    }
]

for person in daten:
    print(f'{person["name"]} ({person["alter"]} Jahre):')
    for kurs, note in person["kurse"]:
        print(f"  {kurs}: {note}")


"""
📌 Liste → Birden fazla kişi
📌 Dictionary → Her kişinin bilgisi
📌 Liste içinde Tuple → Dersler ve notlar

🗣 Türkçe Özet:
Yapı	                        Açıklama
📌Liste içinde Tuple	        Sıralı ve sabit veriler
📌Liste içinde Dict	            Her eleman detaylı bilgi (örneğin kişi)
📌Dict içinde Liste	            Tek anahtar, birden fazla değer
📌Dict içinde Tuple	            Koordinatlar, sabit değer çiftleri

"""

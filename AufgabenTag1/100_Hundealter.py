
# Hundealter

# Hundeliebhaber stellen sich häufig die Frage,
# wie alt ihr Hund wohl wäre, wenn er kein Hund, sondern ein Mensch wäre.
# Landläufig rechnet man Hundejahre in Menschenjahre um,
# indem man das Alter des Hundes mit 7 multipliziert.
# Je nach Hundegröße und Rasse sieht die Umrechnung jedoch etwas komplizierter aus,
# z.B.:
# - Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
# - 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
# - Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

# Schreibe ein Programm, das das Alter eines Hundes erfragt und dann nach obiger
# Methode berechnet, welchem Alter in Menschenjahren das entspricht.
print("Möchten Sie Alter von Ihres Hundes  berechnen?")
eingabe= int(input("Wenn Ja, geben Sie Ihr Hund alt ein: "))

if eingabe==1:
    print("Ihr Hund entsprechend 14-jährigen Menschen")
elif eingabe==2:
    print("Ihr Hund entsprechend  22-jährigen Menschen")

elif eingabe>2:
    menschenalter = 22+(eingabe-2)*5
    print(f"Ihr Hund entspricht einem {menschenalter}-jährigen Menschen.")
else:
    print("Ungültige Eingabe. Das Alter muss mindestens 1 sein.")
